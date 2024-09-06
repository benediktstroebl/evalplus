
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
    # arr = [1,2,3,5,4,7,9,6]
    # palindrome = 3,4,5,4,3,2,1,2
    # palindrome = 3,4,5,4,3,2,2,1
    # palindrome = 2,1,2,3,2,1,2,3

    # Start by copying the array
    # Run a for loop over the array
    # Take the first element in the array
    # Using a while loop, start adding elements to the palindrome while their difference is greater than zero.
    # If the difference is greater than zero, check if the current element is greater or lower than the array's element.
    # If it's greater, subtract the element from the current element. If it's lower, add the element to the current element.

    palindrome = []
    count = 0

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            palindrome.append(arr[i])
            count += 1

    return count

