
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
    #if array length is odd then set middle index to be a pivot and move outwards from pivot
    #if length of array is even then set middle two indexes as pivot and move outwards
    #compare array index and reverse index. If different, increment counter. Continue until index and reverse index meet
    #if they meet and equal, return counter
    #if they meet and equal, return counter.
    #if they don't meet, return counter + (length of array - length of palindrome)
    if len(arr) % 2 != 0:
        middle = len(arr)//2
        pivot = middle
        reversed_pivot = len(arr)-middle-1
    else:
        middle = (len(arr)-1)//2
        pivot = middle
        reversed_pivot = middle

    #initialize counter variable
    counter = 0

    #if there are no palindromic elements, return length of array - length of palindrome
    if pivot == reversed_pivot:
        return len(arr) - (2 * pivot)

    while pivot != reversed_pivot and arr[pivot] != arr[reversed_pivot]:
        counter += 1
        if pivot < reversed_pivot:
            pivot += 1
        else:
            reversed_pivot -= 1
    return counter

