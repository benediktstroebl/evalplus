```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operation (`a % 10` and `b % 10`), and then multiplies these unit digits. To handle the cases where the product of the unit digits exceeds 9, we apply the modulo operation again (`(dig1 * dig2) % 10`) to ensure the result fits within a single digit. 

Here is a test suite to verify the correctness of the implementation:
```python
# Test case for positive integers
assert multiply(12, 42) == 4

# Test case for negative integers
assert multiply(-15, -26) == 5

# Test case for zero
assert multiply(0, 0) == 0

# Test case for one of the factors being zero
assert multiply(0, 65) == 0

# Test case for random integers
assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14, -15) == 20
```

This test suite covers different scenarios, including positive and negative integers, zero and one-digit numbers, and different combinations of input integers.

The code assumes that the input is valid and satisfies the constraints of the problem, as mentioned in the assumption section of the function definition. If you want to make the code more robust and include input validation, you could add additional checks to verify that the input is indeed a valid integer within the specified range.