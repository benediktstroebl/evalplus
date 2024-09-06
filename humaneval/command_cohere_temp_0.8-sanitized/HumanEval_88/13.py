def sort_array(array):
    odd, even = array[:1], array[1:]
    odd = odd[::-1] if sum(odd) % 2 else odd
    return even + odd