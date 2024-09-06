from collections import *
def pluck(arr):
    # Your code here!
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []
    min_even_value = min(even_values)
    min_index = even_values.index(min_even_value)
    return [min_even_value, min_index]