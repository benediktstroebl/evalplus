def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:] if array == [] else sorted(array)
    else:
        return sorted(array, reverse=True) if array == [] else sorted(array)