```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits of `a` and `b` and returns the result. Notably, the modulo operation (`% 10`) is used twice to ensure that the output is also a single-digit number, irrespective of the size of the input numbers. 

To validate the correctness of the function, the following tests could be conducted:
```python
# Test Case 1
test_mult = [148, 412]
expected_result = 16
result = multiply(*test_mult)
assert result == expected_result

# Test Case 2
test_mult = [19, 28]
expected_result = 72
result = multiply(*test_mult)
assert result == expected_result

# Test Case 3
test_mult = [2020, 1851]
expected_result = 0
result = multiply(*test_mult)
assert result == expected_result

# Test Case 4
test_mult = [14, -15]
expected_result = 20
result = multiply(*test_mult)
assert result == expected_result
```

These tests cover distinct cases, including positives, negatives, and zeros, to confirm the robustness of the `multiply` function.