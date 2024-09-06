
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

    # if array is empty, it is already palindromic.
    if len(arr) == 0:
        return 0
    # if array is not palindromic, we want to keep track of the number of changes
    # we make so that we can determine the smallest number.
    n_changes = 0
    i = 0
    j = len(arr) - 1

    while i < j:
        # if arr[i] and arr[j] are the same, skip them.
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        # if arr[i] and arr[j] are not the same, we need to check if swapping the
        # values will make the array palindromic
        else:
            # temp_arr is an array with arr[i] and arr[j] swapped
            temp_arr = arr[:]
            temp_arr[i] = arr[j]
            temp_arr[j] = arr[i]
            # if the temp_arr is not palindromic, that means we have to change the
            # value at i and j to make the array palindromic
            if temp_arr == temp_arr[::-1]:
                n_changes += 1
                i += 1
                j -= 1
            # if the temp_arr is palindromic, we have to check to see if the
            # remaining array after removing i and j is palindromic
            else:
                front_arr = arr[:i]
                back_arr = arr[i + 1 : j + 1]
                # if the front_arr and back_arr are not palindromic, we have to change the
                # values at i and j.
                if front_arr != front_arr[::-1] or back_arr != back_arr[::-1]:
                    n_changes += 1
                    i += 1
                    j -= 1
                # if the front_arr and back_arr are palindromic, we have to change the
                # values at i and j but we have to account for how many changes we need to
