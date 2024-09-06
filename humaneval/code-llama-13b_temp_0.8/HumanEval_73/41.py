
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

    """
    def change_palindrome(arr, len_arr):
        # count how many changes are needed for the array to be palindrome
        count = 0

        # check if array is empty or has only one element
        if len_arr == 0 or len_arr == 1:
            return 0
        elif len_arr == 2:
            return 1

        # convert array into list for mutability
        arr = list(arr)

        # iterate through list from both ends, left and right
        left = 0
        right = len_arr - 1

        # count only till middle of the array
        while left < right:
            # if the elements are not equal, we need to make a change
            if arr[left] != arr[right]:
                # check if current left element is not equal to the right element
                if arr[left] != arr[right-1]:
                    count += 1
                    arr[right] = arr[left]

                # check if current right element is not equal to the left element
                elif arr[right] != arr[left+1]:
                    count += 1
                    arr[left] = arr[right]

            # move to next element
            left += 1
            right -= 1

        return count
    """

    # make a copy of the input array
    arr = arr.copy()
    # sort the array in ascending order
    arr.sort()

    # start with 0 as a total number of changes needed
    count = 0

    # loop through the array from both ends, left and right
    left = 0
    right = len(arr) - 1

    # loop till middle of the array
    while left < right:
        # if the elements are not equal
        if arr[left] != arr[right]:
            # increment total number of changes needed
            count += 1

            # if the current left element is not equal to the right element
            if arr[left] != arr[right-1]:
                # change the right element to the left element
                arr[right] = arr[left]

            # if the current
