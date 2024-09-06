
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
    if len(arr) <= 1:
        return 0

    # 1. Create a mirrored array and fill with zeros
    mirror = [0] * len(arr)

    # 2. Start in the middle of the array and fill the mirror with the corresponding array values
    middle_index = len(arr) // 2
    for i in range(middle_index):
        mirror[i] = arr[-i-1]

    # 3. Fill the second half of the mirror
    for i in range(middle_index, len(arr)):
        mirror[i] = arr[i-middle_index]

    # 4. Find the differences between the two arrays and count the differences
    count = 0
    for i in range(len(arr)):
        if mirror[i] != arr[i]:
            count += 1

    return count
