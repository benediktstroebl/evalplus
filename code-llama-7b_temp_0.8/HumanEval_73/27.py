
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
    # sanity check
    if not isinstance(arr, list) or len(arr) == 0:
        return 0

    # set initial values
    palindrome = arr[:]
    subarray = arr[:]
    subarray_counter = 0

    # special cases
    if len(subarray) == 1:
        return 0
    elif len(subarray) == 2:
        if subarray[0] == subarray[1]:
            return 0
        else:
            return 1

    # sort list
    subarray.sort()

    # calculate how many times the smallest element occurs
    smallest_element_counter = subarray.count(subarray[0])

    #  print("smallest element counter: ", smallest_element_counter)

    # check for palindromic subarrays
    palindrome_counter = 0

    # print("arr:", arr)

    # check if first half of the subarray is palindromic
    for i in range(len(subarray)):
        if subarray[i] == subarray[-(i+1)]:
            palindrome_counter += 1
        else:
            break

    # print("palindrome_counter: ", palindrome_counter)

    # check if the second half of the subarray is palindromic
    # count how many items are in the second half
    items_in_second_half = len(subarray) - palindrome_counter

    # print("items_in_second_half: ", items_in_second_half)

    # check if second half is palindromic
    # if second half is palindromic, then the total number of operations will be equal to the smallest_element_counter
    if subarray[palindrome_counter] == subarray[-palindrome_counter-1]:
        subarray_counter = smallest_element_counter
    else:
        # print("second half not palindromic")
        # check how many items in the second half are greater than the last element
        for i in range(items_in_second_half, len(subarray)):
           
