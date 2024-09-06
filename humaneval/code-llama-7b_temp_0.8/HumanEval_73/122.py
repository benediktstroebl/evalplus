
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
    #
    # 1. Find the array's length
    # 2. Iterate through the array backwards to check for a palindrome.
    # 3. If we find a palindrome, return 0.
    # 4. If we don't find a palindrome, iterate again through the array to count how many mismatches there are.
    # 5. If there are an odd number of mismatches, return the total mismatches minus one.
    # 6. Otherwise, return the total mismatches.
    #
    length = len(arr)
    found = False
    mismatches = 0

    for i in reversed(range(length)):
        for j in reversed(range(i, length)):
            if arr[i] == arr[j]:
                found = True
                break
        if found:
            break

    if found:
        return 0

    for i in range(length):
        for j in reversed(range(i + 1, length)):
            if arr[i] != arr[j]:
                mismatches += 1

    return mismatches if mismatches % 2 == 0 else mismatches - 1

