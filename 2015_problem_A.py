#!/usr/bin/env python

from math import cos, sin, radians
from sys import argv, setrecursionlimit

# price(k) = p * (sin(a * k + b) + cos(c * k + d) + 2)
def price(p, a, b, c, d, k):
	return p * (sin(a * k + b) + cos(c * k + d) + 2)

def largest_decline(prices):
	declines = []
	def helper(prices, declines):
		head = prices[0]
		tail = prices[1:]
		try:
			declines.append(head - min(tail))
		except (IndexError, ValueError):
			declines.sort()
			return declines[len(declines)-1]
		return helper(tail, declines)
	return helper(prices, declines)

def segment_input(prices):
	segments = []
	def helper(prices, segments):
		head = prices[0]
		for index in xrange(1, len(prices)):
			if prices[index] > head:
				segment = prices[:index]
				if len(segment) > 1:
					segments.append(segment)
				return helper(prices[index:], segments)
		segments.append(prices)
		return segments
	return helper(prices, segments)


# def main():
# 	p, a, b, c, d, n = argv[1:]
# 	prices = []
# 	for i in xrange(1, int(n)+1):
# 		prices.append(price(int(p), int(a), int(b), int(c), int(d), i))
# 	return largest_decline(prices)

def main():
	p, a, b, c, d, n = argv[1:]
	prices = []
	declines = []
	for i in xrange(1, int(n)+1):
		prices.append(price(int(p), int(a), int(b), int(c), int(d), i))
	segments = segment_input(prices)
	for segment in segments:
		declines.append(segment[0] - min(segment))
	return max(declines)


if __name__ == '__main__':
	setrecursionlimit(1500)
	answer = main()
	print answer
