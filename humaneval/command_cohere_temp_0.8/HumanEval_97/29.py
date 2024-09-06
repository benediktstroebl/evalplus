```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits of `a` and `b` and returns the result. This is done using the `%` operator to calculate the residue of each integer and then multiplying these residues, finally, the result is cast back to an integer using the `%` operator to obtain the product of the unit digits. 

To test this script, you can write a couple of test cases alongside their expected outputs like so:
```python
test_cases = [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20)
]

for a, b, expected in test_cases:
    output = multiply(a, b)
    assert output == expected
```

This script provides a simple and efficient solution to the problem statement.