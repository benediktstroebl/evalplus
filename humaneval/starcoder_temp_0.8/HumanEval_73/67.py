
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
    # We will sort the array and then check to see how many numbers we need to swap in order to turn the
    # array into a palindrome.
    # We will iterate through the array and check if the number at that index is the same as the number
    # at the same index from the end of the array. If it is, we will skip that index and move on. If the
    # numbers are not the same, we will swap the numbers, and then we will iterate through the array again
    # and check to see if we have made the array palindromic.
    # If we have, we will return 0. If we do not have, we will count up the number of swaps needed and return
    # that value.
    #
    # We will keep track of the current index and the current number in the for loop. If the current number
    # is equal to the number from the end of the array, we will set the current index to the value of
    # len(arr)-1. Otherwise, we will set the current index to the current index plus one. We will then swap
    # the current number and the number from the end of the array.
    #
    # The reason we check to see if the current number is equal to the number from the end of the array
    # is that if we reach the end of the array and the current number is equal to the number from the end
    # of the array, we will still be able to turn the array into a palindrome by swapping the two numbers.
    #
    # The runtime of this algorithm is O(n^2) and the space complexity is O(n).

    # Sort the array
    arr.sort()
    # Keep track of the current index
    current_index = 0
    # Keep track of the current number
    current_number = arr[current_index]
    # We will keep swapping numbers until the array is a palindrome
    while current_number!= arr[-1]:
        # If the current number is equal to the number from the end of the array, we can still
        # turn the array into a palindrome by swapping the two numbers.
        if current_number == arr[-(current_index+1)]:
            # We will set the current index to the value of len(arr)-1
            current_index = len(arr)-1
        else:
            # We will swap the current number and the number from
