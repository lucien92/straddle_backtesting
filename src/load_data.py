import pandas as pd

class data:
    def __init__(self, stock, period):
        self.stock = stock
        self.period = period
        self.data = yf.download(stock, period=period)
    def save(self, path):
        self.data.to_csv(path)
    def load_from_csv(self, path):
        self.data = pd.read_csv(path)
        return self.data
    def show(self):
        return self.data