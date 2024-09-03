```python
def digits(n):
"""Given a positive integer n, return the product of the odd digits.
Return 0 if all digits are even.

Example:
1) digits(1)  == 1
2) digits(4)  == 0
3) digits(235) == 15
"""
    prod = 1
    n = str(n)
    for digit in n:
        if int(digit) % 2 == 1:
            prod *= int(digit)
        else:
            return 0
    return prod
```