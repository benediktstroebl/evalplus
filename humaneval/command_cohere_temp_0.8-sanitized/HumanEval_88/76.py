def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:len(array)//2+1:-1]
    else:
        return array[::-1]