Here's a Python script that implements the `by_length` function with tests to validate its correctness:
```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = sorted(filtered_digits, reverse=True)
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [names[i] for i in reversed_digits]

# Test cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
expected1 = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length(arr1) == expected1

arr2 = []
assert by_length(arr2) == []

arr3 = [1, -1, 55]
expected3 = ['One']
assert by_length(arr3) == expected3

```

The tests assert that the function works correctly for the given examples. The function first sorts the array of integers, then filters out only the digits that are between 1 and 9, then reverses the array of digits, and finally returns the names of the digits in reverse order.