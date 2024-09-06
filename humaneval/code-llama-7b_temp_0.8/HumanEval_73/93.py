
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
    # key: element; value: number of occurrences of that element
    occurrences = dict()
    for x in arr:
        occurrences[x] = occurrences.get(x, 0) + 1

    # palindrome = # of elements in arr that only appear an odd number of times
    palindrome = 0
    for num in occurrences:
        if occurrences[num] % 2 == 1:
            palindrome += 1
            # If we have an odd number of the same element, we can remove one and be left with an even number
            occurrences[num] -= 1

    # remaining elements that are not part of palindrome are those that are present an even number of times
    total = palindrome
    for num in occurrences:
        total += occurrences[num] // 2

    return total
