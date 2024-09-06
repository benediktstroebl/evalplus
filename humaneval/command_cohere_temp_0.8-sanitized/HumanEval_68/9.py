from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_values = [num for num in accumulate(arr) if num % 2 == 0]
    return [min(even_values), min(Counter(even_values).items(), key=lambda x: x[1])[0]] if even_values else []