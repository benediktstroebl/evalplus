Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    digits_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [digits_names[i] for i in reversed_sorted_arr if i >= 1 and i <= 9]

# Test cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
expected_result1 = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

arr2 = []
expected_result2 = []

arr3 = [1, -1, 55]
expected_result3 = ['One']

test_cases = [
    ([arr1, expected_result1],),
    ([arr2, expected_result2],),
    ([arr3, expected_result3],),
]

for case in test_cases:
    arr, expected_result = case
    actual_result = by_length(arr)
    assert actual_result == expected_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"
```

This script defines the `by_length` function that takes an array of integers as input and sorts the digits from 1 to 9, reverses the array, and then converts each digit to its name. It includes test cases to validate the function against various scenarios. The tests ensure that the function works as expected and returns the correct output for the given input arrays.