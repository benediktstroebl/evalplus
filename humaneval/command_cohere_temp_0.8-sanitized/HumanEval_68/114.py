from collections import Counter
def pluck(arr):
    if not arr:
        return []

    # Count the nodes with the smallest even value and their positions
    even_values = Counter(val for val in arr if val % 2 == 0)
    smallest_even_index = min(even_values, key=even_values.get)

    # Return the smallest even value and its index
    return [smallest_even_index, even_values[smallest_even_index]]
arr = [4, 2, 3]