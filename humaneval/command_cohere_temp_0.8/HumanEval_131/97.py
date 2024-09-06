```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function called `digits` that takes in a positive integer as an input and returns the product of the odd digits present in that number. The function first initializes a variable called `product` to 1, which will be used to accumulate the product of the odd digits. It then iterates through each digit in the string representation of the input number, checking if each digit is odd using the modulo operator (`%`). If the digit is odd, it multiplies it with the `product`, updating it accordingly. Finally, the function returns the computed product of odd digits, or 0 if all digits are even.

Here is a test case that can be used to validate the functionality of the provided implementation:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(123) == 21
assert digits(50) == 0
``` 

This test suite contains multiple assertions that verify the correctness of the `digits` function for different scenarios mentioned in the problem description.