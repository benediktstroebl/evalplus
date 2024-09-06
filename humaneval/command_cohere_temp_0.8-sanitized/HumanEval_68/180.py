import bisect
import unittest
def pluck(arr):
    # Use bisect to find the smallest even value and its index
    even_values = [x for x in arr if x % 2 == 0]
    if even_values:
        min_value = min(even_values)
        min_index = bisect.bisect_left(even_values, min_value)
        return [min_value, min_index]
    # If no even values, return empty list
    return []