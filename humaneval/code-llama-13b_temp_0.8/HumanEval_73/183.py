
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
    if not arr:
        return 0
    n = len(arr)
    n_changes = 0
    # first check to see if there are any duplicate elements
    if len(set(arr)) == len(arr):
        return n

    # if there are duplicates, count the number of each element and find the max number of each
    # element that is palindrome
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    num_palindromes = {}
    for i in counts:
        num_palindromes[i] = counts[i] // 2

    # the total number of changes to be made is equal to the number of elements not found in the
    # palindromes dict
    n_changes = n - sum(num_palindromes.values())
    return n_changes


