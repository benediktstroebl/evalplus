from collections import Counter
from collections import defaultdict
def pluck(arr):
    even_count = Counter(n for n in arr if n % 2 == 0)
    min_idx = defaultdict(lambda: float('inf'))
    for idx, val in even_count.items():
        min_idx[val] = idx

    smallest_even = min(even_count, key=even_count.get)
    result = [smallest_even, min_idx[smallest_even]]
    
    return result if result[0] != 0 else []