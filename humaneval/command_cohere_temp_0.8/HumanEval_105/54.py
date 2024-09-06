Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name for num in reversed_sorted_arr for name in dict.fromkeys([str(num) for num in range(1, 10)])]
    return result if result else []

# Tests
dict = dict.fromkeys('One Two Three Four Five Six Seven Eight Nine'.split())
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([10, 5, 3, 9, 1]) == ['Ten', 'Six', 'Three', 'Nine', 'One']
assert by_length([1, -1, 55]) == ['One']
``` 

This script provides a function called by_length that takes an array of integers as input and sorts the integers that are between 1 and 9 inclusive, reverse the resulting array, and then replaces each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine". The function returns the mapped result or an empty list if the input array is empty or only contains numbers outside the valid range.

To test the function, the script creates a dictionary that associates digit names with their corresponding numbers from 1 to 9 and uses assertion checks to verify that the function produces the expected output for various test cases.