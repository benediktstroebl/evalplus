def sort_array(array):
    odd, even = sorted(array), sorted(array, reverse=True)
    return odd if sum(array[0], array[-1]) % 2 else even