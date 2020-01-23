#!/usr/bin/python

import argparse

# find the maximum difference between the smallest and largetest prices
# max profit, subtract a price by another price thats before it

def find_max_profit(prices):
  if len(prices) <= 1:
    return 0
  
  profit = 0
  low = prices[0]
  for i in range(1, len(prices)):
    if prices[i] < low:
      low = prices[i]
    else:
      profit = max(prices[i] - low, profit)
      
  return profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))