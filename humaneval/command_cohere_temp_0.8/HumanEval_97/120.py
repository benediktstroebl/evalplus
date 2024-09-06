```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits to obtain a candidate result. If this candidate result is greater than 9, it means there are carryovers, and the function resets the result to 0 to ensure the final output is a single digit. 

This solution focuses on simplicity while maintaining a clear understanding of the carryover concept. Let's explore a more efficient approach that delivers the same result.

---

Below is an alternative solution that employs a more efficient methodology, achieving the same outcome:
```python
def multiply(a, b):
    dig1, dig2 = a % 10, b % 10
    return int(str(dig1 * dig2)[:1])
```

In this approach, we:
1. Extract the unit digits of both numbers using `a % 10` and `b % 10`.
2. Multiply the unit digits, which gives us a number with many digits.
3. Convert this product to a string.
4. Keep the first digit of this string, using `int(str(dig1 * dig2)[:1])`, ensuring a single-digit result.

This method creatively avoids the need for a loop or explicit tracking of carryovers, achieving both simplicity and efficiency.