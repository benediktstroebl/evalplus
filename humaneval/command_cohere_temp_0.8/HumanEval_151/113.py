```python
def double_the_difference(lst):
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            result += n**2
    return result
```

The function iterates through each number in the list, and if it's an integer and greater than zero, it adds its square to the `result`. This squared value is what gives the odd-numbered values their weightiness in the final sum. The function returns 0 if the input list is empty, and it also disregards non-integer or negative numbers, making the function versatile for various input scenarios. 

Here's a test script to ensure it works correctly for different cases:
```python
test_cases = [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    ([], 0),
    ([], 0),
    (None, None),
    (# An empty string is not an empty list, so it's not valid input #)
    (#(""), #),
]

for numbers, expected in test_cases:
    actual = double_the_difference(numbers)
    assert actual == expected, f"For input {numbers}, expected {expected}, but got {actual}"
```

This test suite covers a variety range of inputs, including empty inputs, to ensure the function behaves as expected.  For the last test case, it is worth noting that an empty string is not considered an empty list, so the function would not handle it as an empty list would. Thus, the expected behavior in that case would be to not evaluate the function due to the invalid input type.  If you intend to support empty strings as valid input, the function can be modified accordingly.