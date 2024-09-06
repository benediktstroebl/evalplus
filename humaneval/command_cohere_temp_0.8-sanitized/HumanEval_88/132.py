def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:] if array == [] else array[:0:-1] or [array[-1]]
    else:
        return array[:] if array == [] else array[:0:-1] or [array[0]]