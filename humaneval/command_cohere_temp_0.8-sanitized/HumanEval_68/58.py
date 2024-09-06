from collections import Counter
def pluck(arr):
    if not arr:
        return []
    
    # Count occurrences of each value and find the smallest even value using Counter
    even_values = Counter(val for val in arr if val % 2 == 0)
    smallest_even_val, _ = min(even_values.items(), key=lambda x: x[1])
    
    # Find the index of the smallest even value using next_index
    smallest_index = arr.index(smallest_even_val)
    
    return [smallest_even_val, smallest_index]