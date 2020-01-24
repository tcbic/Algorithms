#!/usr/bin/python

import argparse

def find_max_profit(prices):
  """This function returns the maximum profit that can be made
  from a single buy and sell. Note that a stock must be bought
  first before it can be sold."""
  # What's the condition under which this function wouldn't run?
  if len(prices) == 1:
    print("Not enough data to determine max profit.")
  else:
    # First possible minimum price.
    current_min_price_so_far = prices[0]
    # Current max profit calculation.
    max_profit_so_far = prices[1] - prices[0]
    # Iterate through prices starting with first possible place to buy.
    for i in prices[1:]:
      if (i - current_min_price_so_far) > max_profit_so_far:
        max_profit_so_far = i - current_min_price_so_far
      # Update current min price if i is smaller.
      if i < current_min_price_so_far:
        current_min_price_so_far = i
  return max_profit_so_far

a = [1050, 270, 1540, 3800, 2]
print(find_max_profit(a))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))