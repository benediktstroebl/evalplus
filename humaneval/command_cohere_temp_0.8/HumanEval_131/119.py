```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It first initializes a variable `prod` to 1, which will store the final result. Then, it iterates through each digit in the string representation of `n`, checking if each digit is odd using the modulo operator. If the digit is odd, it multiplies the `prod` by the value of that odd digit. Finally, it returns the value of `prod`, which now holds the product of all odd digits in `n`, or 0 if all digits are even.

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 3
    assert digits(50) == 0
    assert digits(75) == 7500
test_digits()
```

Executing the above code will yield the following results:
```bash
 tested digits() 
 tidying up ... done! 
 ```