
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
    # if the list is already palindrome, just return 0
    if arr == arr[::-1]:
        return 0

    # if the list is not palindrome, compare the first item to the last item,
    # and the second to the second-to-last item, etc.
    # if any of the item is not equal to the corresponding reversed one, return 1
    # if any of the item is equal to the corresponding reversed one, keep comparing

    # need to consider three scenarios here:
    # 1. if the first item is not equal to the last one, we need to change 1
    # 2. if the first item is equal to the last one, we need to check if the second one is equal to the second-to-last one
    # 3. if the second item is not equal to the second-to-last one, we need to change 1
    # 4. if the second item is equal to the second-to-last one, we need to check if the third one is equal to the third-to-last one
    # ......

    # since we only care if any of the element is not equal to the corresponding reversed one,
    # we don't need to compare more than 2 elements at a time
    # can we do this in one for loop?
    # how do we know how many comparisons to make?

    # if we can do this in one loop, then the time complexity will be O(n)
    # how do we get the answer?
    # what is the maximum number of changes we can do in 2 iterations?
    # what is the minimum number of changes we can do in 2 iterations?
    # if we take 2 iterations, we can get the minimum number of changes
    # we can also get the maximum number of changes
    # can we do this in one iteration?

    count = 0
    i = 0
    j = len(arr) - 1

    while i < j:
        # if the first item is not equal to the last one, we need to change 1
        if arr[i] != arr[j]:
            count += 1
            i += 1
            j -= 1
