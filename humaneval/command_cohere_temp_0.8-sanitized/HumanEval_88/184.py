def sort_array(array):
    odd, even = array[:1], array[-1:]
    return odd + even if sum(odd + even) % 2 else even + odd