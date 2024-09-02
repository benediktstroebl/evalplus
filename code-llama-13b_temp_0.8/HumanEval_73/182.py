
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
    end = len(arr)

    # Counting the number of occurrences of each element
    count_dic = {}
    for i in arr:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1

    # Removing the middle element if there is an odd number of elements
    if len(arr) % 2 == 1:
        del count_dic[arr[end//2]]
        end -= 1

    # Number of palindrome changes
    change = 0
    # Number of the remaining elements
    remaining = end // 2

    # While there are elements remaining and there are more than 1 element of
    # the same value, calculate the number of changes needed and remove them
    for i in count_dic.values():
        while i >= 2:
            change += 1
            i -= 2
            remaining -= 1

    # If there are an odd number of elements, change one of the remaining element
    if remaining > 0:
        change += 1

    return change
