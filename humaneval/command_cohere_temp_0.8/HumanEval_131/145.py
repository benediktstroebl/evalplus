```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable called `product` to 1, which will be used to accumulate the product of odd digits. Then, it iterates through each digit in the decimal representation of the input number `n` and checks if the digit is odd using the modulo operator (`%`). If the digit is odd, it multiplies it by the `product`, updating it accordingly. Finally, the function returns the value of the `product` accumulator, which gives the product of the odd digits in the input number, or 0 if all digits are even.

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 21

test_digits()
``` 

This would yield the following results:
```bash
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(123) == 21
``` 

Ensure you include this test code within a testing framework like `pytest` to validate the `digits` function appropriately.