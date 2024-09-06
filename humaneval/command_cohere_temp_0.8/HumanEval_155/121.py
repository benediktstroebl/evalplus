Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            even_count += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_count += 1
    return (even_count, odd_count)
```

This function evaluates the parity of each digit in the num_str, and returns the parity count as a tuple. 

To test this function, you can run the following code:
```python
test_cases = [
    (-12, 1, 1),
    (123, 1, 2),
    (10, 1, 1)
]
for n, expected_even, expected_odd in test_cases:
    result = even_odd_count(n)
    assert result == (expected_even, expected_odd)
```

This will successfully check that the function behaves as expected for a variety of input values.