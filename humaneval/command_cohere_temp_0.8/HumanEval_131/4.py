```python
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1) == 1
    digits(4) == 0
    digits(235) == 15
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Expected a non-negative integer input")
    
    result = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            result *= digit
        n = int(n / 10)
    
    return result
```

This function accepts a positive integer `n` as input and calculates the product of its odd digits. It returns 0 if all digits are even. The function checks if the input is a valid positive integer and raises a `ValueError` if it's not. Additionally, it efficiently processes each digit in the integer's decimal representation while handling the carry from the multiplication.