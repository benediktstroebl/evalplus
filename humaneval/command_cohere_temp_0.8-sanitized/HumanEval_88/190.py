def sort_array(array):
    odd, even = False, False
    if sum(array[0], array[-1]) % 2 == 1:
        odd = True
    if sum(array[0], array[-1]) % 2 == 0:
        even = True
    if odd:
        array[:] = sorted(array, reverse=False)
    if even:
        array[:] = sorted(array, reverse=True)
    return array