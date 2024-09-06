```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operation (`a % 10` and `b % 10`), and then multiplies these unit digits. The result is again reduced to the unit digit using the modulo operation (`(dig1 * dig2) % 10`) to ensure the final result fits within the range of a single digit, as per the problem statement. 

This solution assumes that input is valid and within acceptable ranges to properly apply the modulo operation. 

To ensure that the solution is correct and adequately general, it's advisable to complement it with a test suite that covers different input scenarios adequately. Here's a simple example:
```python
def test_multiply():
    assert multiply(10, 5) == 0
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20
```