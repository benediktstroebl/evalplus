def sort_array(array):
    if len(array) == 0:
        return array
    odd, even = divmod(sum(array[::-1]), 2)
    if odd:
        return sorted(array, reverse=True)
    else:
        return sorted(array)