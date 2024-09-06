
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
    # [1,2,3,5,4,7,9,6]
    # [1,2,3,4,3,2,2]
    # [1,2,3,2,1]

    # [1,2,3]
    # [1,2,4]

    # [1,2,3,4,3,2,2]
    # [1,2,4,2,1]

    # [1,2,3,2,1]
    # [1,2,4,2,1]
    # [1,2,3,2,1]

    # [1,2,3,5,4,7,9,6]
    # [1,2,4,4,3,2,2]
    # [1,2,4,4,3,2,2]
    # [1,2,4,4,3,2,2]
    # [1,2,4,4,3,2,2]

    if len(arr) <= 1:
        return 0

    foreground_arr = [0] * len(arr)
    background_arr = foreground_arr[:]

    foreground_arr[0] = 1
    foreground_arr[-1] = 1

    while True:
        foreground_sum = sum(foreground_arr)
        background_sum = sum(background_arr)

        if foreground_sum == background_sum:
            break
        elif foreground_sum > background_sum:
            # swap
            foreground_arr, background_arr = background_arr, foreground_arr
        else:
            # find min
            # find max
            foreground_min_index = foreground_max_index = None
            foreground_min = foreground_max = 0
            for i in range(1, len(foreground_arr) - 1):
                if foreground_arr[i] < foreground_min:
                    foreground_min_index = i
                    foreground_min = foreground_arr[i]

                if foreground_arr[i]
