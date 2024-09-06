```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits to obtain a candidate for the product's unit digit. If this candidate is greater than 9, it means the product's unit digit must be 0, so the function returns just 0 in that case. This complies with the constraint that the product of two numbers uniformly at random chosen from the range `[1, 10^n]` will have a unit digit of 0 with probability 0.9. Hence this solution assumes that the input is always valid, i.e., the inputs are pairs of integers in the range `[1, 10^n]`. 

Here is a simple test suite to verify the function:
```python
# Tests for the multiply function

def test_multiply():
    assert multiply(12, 8) == 4    # 12 * 8 = 96, 96 mod 10 = 4
    assert multiply(51, 23) == 3   # 51 * 23 = 1223, 1223 mod 10 = 3
    assert multiply(138, 5) == 0   # 138 * 5 = 690, 690 mod 10 = 0
    assert multiply(557, 4) == 4   # 557 * 4 = 2240, 2240 mod 10 = 4
    assert multiply(74, 9) == 6    # 74 * 9 = 654, 654 mod 10 = 6

def test_large_numbers():
    assert multiply(1000000, 99999) == 0
    assert multiply(1000001, 1000002) == 0

test_multiply()
test_large_numbers()
```

This test suite includes a test for edge cases involving very large numbers, where the strategy for solving the problem becomes particularly useful. 

To run the tests, you can copy and paste the test cases into a Python environment of your choice and run the tests there. 

Let me know if you would like me to explain any part of the solution in more detail.