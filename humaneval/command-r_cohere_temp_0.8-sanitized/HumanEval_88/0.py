def sort_array(array):
    """
    Sort the array based on the condition specified.
    Don't change the given array, return a sorted copy instead.
    """
    sorted_array = array[:]
    if sum(array[0], array[-1]) % 2 == 1:
        sorted_array.sort()
    else:
        sorted_array.sort(reverse=True)
    return sorted_array