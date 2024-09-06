def sort_array(array):
    odd, even = array[:1], array[1:]
    odd, even = odd + reversed(even), even + reversed(odd)
    return odd + even