```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is built by reading the same backwards
    and forwards.
    """
    initial check for isPalindrome(arr)
    """
    if isPalindrome(arr):
        return 0
    else:
        n = len(arr)
        half = n // 2
        min_change = n - 1
        for i in range(half):
            temp = arr[i]
            for j in range(i + 1, half):
                arr[j] = arr[i]
                arr[i] = temp
                min_change = min(min_change, n - arr[half + i] - arr[half + j])
        return min_change

def isPalindrome(arr):
    """
    Check if the given array is palindrome
    """
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True
``` 
The function is designed to find the minimum number of elements needed to to turn an array into a palindrome. It achieves this goal by iteratively switching elements in the array to their reverse counterparts until the array becomes palindrom.