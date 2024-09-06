from collections import Counter
def pluck(arr):
    even_count = sum(1 for n in arr if n % 2 == 0)

    if even_count == 0:
        return []

    # Find the smallest even value and its index
    smallest_val, smallest_index = min(Counter(arr).items(), key=lambda x: x[0])
    
    return [smallest_val, smallest_index]