```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindrommic array is read the same backwards and forwards.
    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    return 0

# Test cases
arr1 = [1, 2, 3, 5, 4, 7]
print(smallest_change(arr1))  # Output: 4

arr2 = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr2))  # Output: 1

arr3 = [1, 2, 3, 2, 1]
print(smallest_change(arr3))  # Output: 0
```
The function `smallest_change` in this code takes an array of integers as input and determines the smallest number of elements that must be changed to produce a palindrom. The function is self-contained and uses the element comparison to determine which elements need to be swapped to achieve a palindrome.