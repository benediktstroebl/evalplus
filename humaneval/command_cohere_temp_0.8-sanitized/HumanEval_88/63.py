def sort_array(array):
    odd, even = array[:1], array[1:]
    odd, even = odd + reversed(even), sorted(even) if sum(odd + even) % 2 else reversed(even)
    return odd + even