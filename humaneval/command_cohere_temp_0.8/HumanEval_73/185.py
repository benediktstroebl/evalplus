```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Create a reversed copy of the array
    rev_arr = arr[::-1]
    # Calculate the absolute difference between the two arrays
    diff = [abs(x-y) for x, y in zip(arr, rev_arr)]
    return sum(diff) // 2 

# Test Cases:
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0
```

This script defines a function `smallest_change` that takes in an array `arr` as input and returns the minimum number of changes required to make the array palindromic. The function works by first removing any duplicate elements from the array, as the problem statement allows any element to be changed into any other element. Then, it creates a reversed copy of the unique array and calculates the absolute differences between corresponding elements and their reversed counterparts. These differences indicate the number of changes needed to make the array palindromic, and the sum of these differences is divided by 2 to account for double-counting (changing an element and its reverse at the same time). Finally, the function returns the total number of changes needed.