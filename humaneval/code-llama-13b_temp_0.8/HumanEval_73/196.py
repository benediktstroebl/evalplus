
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
    odd_count = 0
    odd_sum = 0

    even_count = 0
    even_sum = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
            even_sum += num
        else:
            odd_count += 1
            odd_sum += num

    if odd_count > 1:
        return len(arr) - even_count - (odd_count - 1)
    return len(arr) - even_count

