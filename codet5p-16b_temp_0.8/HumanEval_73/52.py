
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

    count = 0
    palindromic_arr = []

    for i in range(len(arr)):
        if len(palindromic_arr) == 0:
            palindromic_arr.append([arr[i]])
        else:
            for j in palindromic_arr:
                j.append(arr[i])
                if j not in palindromic_arr:
                    palindromic_arr.append(j)
                    count += 1
    return count

