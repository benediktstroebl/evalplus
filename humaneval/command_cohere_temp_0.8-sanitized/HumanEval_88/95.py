def sort_array(array):
    odd = len(array) % 2
    if odd:
        array = reversed(array)
    array.sort()
    if odd:
        array = reversed(array)
    return array