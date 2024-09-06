
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
    # Write your code here.
    palindrome = []
    count = 0
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            palindrome.append(arr[i])
    if len(arr) == len(palindrome):
        return 0
    if len(arr) < len(palindrome):
        palindrome = palindrome[:len(arr)]
    for i in range(0,len(arr)-1):
        if arr[i] != arr[i+1]:
            if palindrome[0] == arr[i]:
                palindrome.pop(0)
                if palindrome[0] == arr[i+1]:
                    palindrome.pop(0)
                    count += 2
                else:
                    count += 1
            else:
                count += 1
        elif arr[i] == arr[i+1] and arr[i+1] == palindrome[0]:
            count += 1
           
