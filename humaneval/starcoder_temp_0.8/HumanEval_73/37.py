
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
    # Create a hash table for each unique element
    # Hash table key: element, value: number of times element appears in arr
    # Elements can be repeated so we should count them.
    hash = {}
    for el in arr:
        if el not in hash:
            hash[el] = 0
        hash[el] += 1

    # Count the number of elements with odd counts
    num_odd = 0
    for key, val in hash.items():
        if val % 2 == 1:
            num_odd += 1

    # Return the number of odd counts minus 1
    return num_odd - 1

