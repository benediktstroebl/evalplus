
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

    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            odd_el_index = i
            break
    else:
        return 0

    palindromic_candidate = arr[:]
    palindromic_candidate[odd_el_index] = arr[odd_el_index] - 1
    palindromic_candidate[odd_el_index+1] = arr[odd_el_index+1] + 1

    return len([x for x in palindromic_candidate if x % 2 == 1])



