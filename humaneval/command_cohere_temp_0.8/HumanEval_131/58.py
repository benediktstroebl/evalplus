```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This problem can be solved by converting the input n into a string and iterating through each digit. If the digit is odd, we multiply it with the `prod` variable, which should be updating the product of all odd digits encountered so far. The provided solution does this in a clean and efficient manner, returning the required product of odd digits for the given input.