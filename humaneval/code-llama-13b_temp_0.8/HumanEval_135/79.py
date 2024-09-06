
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # 1. Create list with the original indexes, to be used later
    index = []
    for i in range(len(arr)):
        index.append(i)

    # 2. Sort the list in reverse order by values in arr
    reverse_arr = sorted(zip(arr, index), key=lambda t: t[0], reverse=True)

    # 3. Loop through the list, comparing indexes, and check if previous is
    # less than or equal to the current. If so, store the index and break out
    # of loop.
    prev = None
    for i in range(len(reverse_arr)):
        if prev and reverse_arr[i][0] < prev:
            return reverse_arr[i][1]
        prev = reverse_arr[i][0]

    return -1
