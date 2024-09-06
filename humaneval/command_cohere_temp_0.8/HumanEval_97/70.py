```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of their unit digits. The expression `a % 10` retrieves the last digit of a (rightmost digit), and `b % 10` does the same for b. Then, `dig1 * dig2` calculates the product of these two unit digits. Finally, the expression `(dig1 * dig2) % 10` ensures the result is modded by 10 and thus truncated to a single digit, which is then returned. 

This solution focuses on the requirement of finding the product of unit digits while ensuring the result fits within a single-digit number.