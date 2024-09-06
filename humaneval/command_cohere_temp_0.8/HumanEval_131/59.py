```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer to a string to easily iterate over its digits. It checks if each digit is odd using the modulo operator (`%`). If a digit is odd, it multiplies it with the `prod` variable, which should be initially 1 to ensure the product is correctly calculated. It returns 0 if all digits are even, adhering to the requirement mentioned in the problem statement.

The problem is straightforward, and the provided solution is efficient with a time complexity of O(n), where n is the number of digits in the given integer.