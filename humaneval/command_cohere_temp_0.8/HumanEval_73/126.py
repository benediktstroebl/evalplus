```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes required to make the array palindromic
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Calculate reverse of array
    arr_reverse = sorted(arr)[::-1]
    return sum(1 for a, b in zip(arr, arr_reverse) if a != b)
```

The function `smallest_change` takes an array of integers as input and returns the minimum number of changes required to make the array palindromic. To achieve this:
- We first convert the array to a list of unique integers using `list(set(arr))`, removing any duplicate values.
- We calculate the reverse of the unique array using `sorted(arr)[::-1]` and zip the original and reverse arrays to compare each element with its corresponding value in the reverse.
- We count the number of elements that differ from their corresponding values in the reverse, using `sum(1 for a, b in zip(arr, arr_reverse) if a != b)`.

This approach efficiently computes the required minimum changes, providing the number of elements that need to be changed to make the original array palindromic.