def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array if odd else reversed(array)) if array else array