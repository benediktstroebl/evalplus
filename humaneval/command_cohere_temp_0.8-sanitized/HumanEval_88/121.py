def sort_array(array):
    odd, even = array[:1], array[-1:]
    if sum(map(len, (odd, even))) % 2 == 0:
        array = sorted(array)[::-1]
    return array