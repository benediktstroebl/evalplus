```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and stores them in `dig1` and `dig2` respectively. It then computes the product of these unit digits and stores the result in `product`. If the product is greater than or equal to 10, it takes the modulo of the product by 10 to ensure that the final result is the unit digit of the correct product.

To test this, you can run the following tests to verify the correctness of the implementation:
```python
# Test Suite
def test_multiply():
    assert multiply(148, 412) == 16, "Expected 16, got {}".format(multiply(148, 412))
    assert multiply(19, 28) == 72, "Expected 72, got {}".format(multiply(19, 28))
    assert multiply(2020, 1851) == 0, "Expected 0, got {}".format(multiply(2020, 1851))
    assert multiply(14, -15) == 20, "Expected 20, got {}".format(multiply(14, -15))

test_multiply()
```

The `test_multiply()` function runs four individual tests, each verifying the correctness of `multiply(a, b)` with a specific input. The `assert` statements check whether the actual output of `multiply(a, b)` matches the expected output for each example. If all assertions pass without any errors, it confirms the correctness of the `multiply()` function. 

Make sure to run this test suite to verify that the implementation is correct.  Please let me know if you have any other questions!