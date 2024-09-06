def sort_array(array):
    odd, even = array[:1], array[1:]
    odd, even = odd + odd[::-1], even + even[::-1]
    return odd + even