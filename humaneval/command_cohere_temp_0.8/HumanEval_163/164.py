Here's a Python script that contains a function named `generate_even_digits` which solves the problem:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a and b, in ascending order.
    """
    # Ensure a is the smallest number by comparing with b first
    if b < a:
        a, b = b, a
    even_digits = []
    while a <= b:
        if a % 2 == 0:
            even_digits.append(a)
        a += 1
    return even_digits
```

The function `generate_even_digits` works by ensuring that the variable `a` is always the smaller of the two given values, which allows us to iterate through numbers without overflowing the smaller number. During each iteration, we check if the current value of `a` is even; if it is, we append it to our `even_digits` list. Lastly, we return this list of even digits.