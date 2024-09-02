
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # A: set up variables for counter and store all the values of the array in set
    count = 0
    elems = set()
    # B: loop over the array
    for num in arr:
        # C: if the num is in the set, then delete it, otherwise add it to the set
        if num in elems:
            elems.remove(num)
        else:
            elems.add(num)
    # D: the amount of numbers we need to change is the half of the length of the set
    count += len(elems) // 2
    # E: if the length of the set is odd, then add 1
    if len(elems) % 2 != 0:
        count += 1
    # F: return the number of numbers we need to change
    return count


                                      s + 2
                                     s
