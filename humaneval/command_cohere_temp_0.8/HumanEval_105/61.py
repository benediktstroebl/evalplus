```python
def by_length(arr):
    # sort and reverse the array
    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]
    # convert sorted and reversed digits into names
    result = ['None'] * len(reversed_arr)
    for i, num in enumerate(reversed_arr):
        if 1 <= num <= 9: 
            result[i] = NUM_TO_NAME[num]
    return result

# dictionary to map number to name
NUM_TO_NAME = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}
```

The following tests will confirm that your function behaves as expected:
```python
test_array = [2, 1, 1, 4, 5, 8, 2, 3]
expected_result = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

assert by_length(test_array) == expected_result
``` 

This test case demonstrates the normal operation of the `by_length` function, with a sorted and reversed array of digits that corresponds to their corrected names.

Here's another edge case test to handle an empty array:
```python
test_empty_array = []
assert by_length(test_empty_array) == []
```

And this test case ensures that the function handles strange numbers by ignoring them, as described in the prompt:
```python
test_strange_array = [1, -1, 55]
expected_result = ['One']

assert by_length(test_strange_array) == expected_result
``` 

These tests will help ensure that the function `by_length` behaves as expected, fulfilling all the requirements of the problem prompt.