Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reverse_sorted_arr = sorted(sorted_arr, reverse=True)
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [names[i] for i in reverse_sorted_arr if i >= 1 and i <= 9]
```

The function `by_length` takes an array of integers as input and sorts the array of integers that are between 1 and 9 inclusive, based on the length of the digits. Then the resulting array is reversed and replaced with the corresponding name of the number. The resulting list is returned after applying the required actions. The above algorithm can be used to solve the given problem.

This script can be tested against sample inputs to ensure it works correctly. Here is a test drive suite for the above function:
```python
def test_by_length():
    # Empty array case
    assert by_length([]) == []

    # Single element case
    assert by_length([8]) == ['Eight']

    # Only negative numbers case
    assert by_length([-1, -2, -3]) == []

    # Only positive numbers case
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']

    # Mixed cases
    assert by_length([-20, -1, 2, 3, 8, 20, 1, 5, 4, 6]) == ['Six', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One', 'Eight']

    # Mixed cases - ignore strange numbers
    assert by_length([1, -1, 55, 3, 8, 20, 4, 5, 7, 9]) == ['Nine', 'Eight', 'Seven', 'Six']

test_by_length()
```

The test drive suite will execute the `by_length` function on a variety of input so as to verify it behaves correctly. You can add more test cases to the test drive suite as needed to cover other scenarios.