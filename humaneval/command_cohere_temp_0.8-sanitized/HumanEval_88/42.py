def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)