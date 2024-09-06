from collections import *
def pluck(arr):
    # Your code here.
    even_values = sorted(v for v in arr if v % 2 == 0)
    if even_values:
        return [min(even_values), even_values.index(min(even_values))]
    else:
        return []