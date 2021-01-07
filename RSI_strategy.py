### Simple RSI Strategy implementation on QuantConnect

class RSIAlgo(QCAlgorithm):

    def Initialize(self):

        # Set our main strategy parameters
        self.SetStartDate(2013,1, 1)   # Set Start Date
        self.SetEndDate(2015,1,1)      # Set End Date
        self.SetCash(10000)            # Set Strategy Cash
        
        RSI_period    = 14                # RSI Look back period 
        self.RSI_OB   = 70                # RSI Overbought level
        self.RSI_OS   = 30                # RSI Oversold level
        self.Allocate = 0.10              # Percentage of captital to allocate
        
        # Add Symbol
        self.AddEquity("AAPL", Resolution.Daily)
        
        self.RSI_indicator = self.RSI("AAPL", RSI_period)
        
        # Ensure that the indicator has enough data before trading
        self.SetWarmUp(RSI_period)
        
        
    def OnData(self, data):
        if not self.Portfolio.Invested:
            if self.RSI_indicator.Current.Value < self.RSI_OS:
                self.SetHoldings("AAPL", self.Allocate)
                
        else:
            if self.RSI_indicator.Current.Value > self.RSI_OB:
                self.Liquidate("AAPL")