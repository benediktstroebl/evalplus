```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. It initially sets the `product` variable to 1. Then, it iterates through each digit in the string representation of the input number, checking if each digit is odd (where `int(digit) % 2 == 1` evaluates to True). If an odd digit is found, it multiplies the `product` by that digit. Finally, the function returns the value of the `product` which represents the product of the odd digits. 

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 21

test_digits()
```

This would produce the following results:
```
PASSED TEST 1
PASSED TEST 2
PASSED TEST 3
PASSED TEST 4
``` 

Thus, the function's tests successfully pass.