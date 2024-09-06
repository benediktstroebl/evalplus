from itertools import accumulate, count
from collections import Counter
def pluck(arr):
    even_values = [val for val in accumulate(arr) if val % 2 == 0]
    if even_values:
        # Get the index of the smallest even value using counter
        min_index = Counter(even_values).most_common()[-1][1]
        return [even_values[min_index], min_index]
    else:
        return []