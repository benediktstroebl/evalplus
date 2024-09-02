
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
    array = arr
    array.sort()
    # print(array)
    def count(array):
        count = 0
        for i in range(len(array)):
            if array[i] != array[len(array) - 1 - i]:
                count += 1
        # print(count)
        return count

    # print(count(array))
    # if count(array) == 0:
    #     return count(array)
    # else:
    count2 = 0
    for i in range(len(array)):
        if array[i] != array[i+1]:
            count2 += 1
        else:
            count2 += 0
    # print(count2)
    # if count2 == 0:
    #     return count2
    # else:
    count3 = 0
    for i in range(len(array)):
        if array[i] != array[i-1]:
            count3 += 1
        else:
            count3 += 0
    # print(count3)
    if
