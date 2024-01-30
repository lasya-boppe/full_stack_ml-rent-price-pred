import pandas as pd

apartment = pd.read_csv('apartment.csv')
gachibowli = pd.read_csv('gachibowli.csv')
jubliee = pd.read_csv('jubliee_hills.csv')
kokapet = pd.read_csv('kokapet.csv')
kompally = pd.read_csv('kompally.csv')
moosapet = pd.read_csv('moosapet.csv')
nizampet = pd.read_csv('nizampet.csv')
somajiguda = pd.read_csv('somajiguda.csv')
tellapur = pd.read_csv('Tellapur.csv')
villa = pd.read_csv('villa.csv')
individual = pd.read_csv('individual.csv')

final = pd.DataFrame()

lst = [apartment, gachibowli, jubliee, kokapet, kompally, moosapet, nizampet, somajiguda, tellapur, villa, individual]

for i in lst:
    final = pd.concat([final, i], axis = 0, ignore_index = True)

print(final)
final.to_csv('FINAL.csv')