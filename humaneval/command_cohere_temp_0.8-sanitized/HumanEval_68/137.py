from itertools import accumulate
def pluck(arr):
    even_values = [x for x in accumulate(arr) if x % 2 == 0]
    if even_values:
        return [min(even_values), even_values.index(min(even_values))]
    return []