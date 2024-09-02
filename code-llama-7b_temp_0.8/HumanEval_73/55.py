
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
    print("arr", arr)
    print(arr[::-1])
    # if the array is a palindrome, we can return 0
    if arr == arr[::-1]:
        return 0
    palindrome = arr[::-1]
    # arr = [1,2,3,5,4,7,9,6]
    # palindrome = [6,9,7,4,5,3,2,1]
    # set the i index to be the front of the array
    i = 0
    # set the j index to be the back of the array
    j = len(arr) - 1
    print(i, j)
    # we're keeping track of the number of changes made
    num_changes = 0
    # while the i index has not reached the middle
    while i < j:
        print("i", i, "j", j)
        # if the i value is smaller than the j value, increment the i index
        if arr[i] > palindrome[j]:
            # increment the i index
            print("increase i")
            i += 1
            # increment the number of changes made
            num_changes += 1
            print("changes", num_changes)
            # return the number of changes
            print("return")
            return num_changes
        # if the j value is smaller than the i value, increment the j index
        elif arr[j] < palindrome[i]:
            # increment the j index
            print("increase j")
            j -= 1
            # increment the number of changes made
            num_changes += 1
            print("changes", num_changes)
            # return the number of changes
            print("return")
            return num_changes
        # otherwise, increment both the i index and j index
        else:
            print("both")
            i += 1
            j -= 1
            print("changes", num_changes)
            # return the number of changes
            print("return")
            return num_changes
    print("end")
    return num_changes
