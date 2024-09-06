```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly computes the product of the unit digits and then iterates on the result if the product is greater than or equal to ten to guarantee a valid unit digit result.

Here is a test suite to verify the correctness of the function:
```python
def test_multiply():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(14, -15) == 20
    assert multiply(2020, 1851) == 0
```

Executing this test suite will definitively show whether or not the function is correct.