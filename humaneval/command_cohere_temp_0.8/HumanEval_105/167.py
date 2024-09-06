```python
def by_length(arr):
    sorted_arr = sorted(arr)
    stripped_arr = [str(n) for n in sorted_arr if 1 <= n <= 9]
    stripped_arr.reverse()
    result = [name for num in stripped_arr for name in num_to_name[num]]
    return result

# Dictionary for number to name conversion
num_to_name = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
```

The function `by_length` takes an array of integers as input and performs the operations described in the problem statement in the following steps:
1. Sort the array: The function first sorts the given array of integers using the `sorted` function.
2. Strip and reverse: Then, it creates a new array `stripped_arr` by iterating through the sorted array and only including integers between 1 and 9. These integers are converted to strings and added to `stripped_arr`. The resulting array is then reversed to obtain the correct order.
3. Replace with names: Finally, the function creates the return array by iterating through the `stripped_arr` and replacing each integer with its corresponding name from the `num_to_name` dictionary.

Note: The `num_to_name` dictionary is defined outside the function for reuse in multiple tests if needed. This dictionary serves as the translation between integer values and their respective names as described in the problem statement.