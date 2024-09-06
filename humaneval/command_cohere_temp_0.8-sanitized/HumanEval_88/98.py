def sort_array(array):
    odd, even = array[:1] + array[-1:], array[1:-1]
    return odd if sum(odd) % 2 else even