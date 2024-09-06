```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array has even length
    if len(arr) % 2 == 1:
        return len(arr) + 1

    # Initialize the variable to the maximum possible number of changes
    changes = len(arr)
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            changes = min(changes, abs(i - (len(arr) - 1 - i)))

    return changes
```

The function takes an array of integers as input and returns the minimum number of changes required to make the array palindromic. The function initially checks if the array length is odd, and returns the array length plus one if so, since a palindrome requires an even length. Then, the function initializes a variable called changes to the current length of the array, which represents the maximum possible number of changes. The function then loops through the array, checking if the first and last elements are equal. If they are not, the function minimizes the changes variable to the absolute difference between the indices of the elements, as this represents the minimum number of changes required to make the array palindromic. The function returns the final value of changes, which represents the minimum number of changes required to make the array palindromic.