def sort_array(array):
    odd, even = False, False
    sum_ = sum(array[:2])
    if sum_%2 == 0:
        even = True
    else:
        odd = True
    if odd:
        array[:] = sorted(array)
    if even:
        array[:] = sorted(array, reverse=True)
    return array