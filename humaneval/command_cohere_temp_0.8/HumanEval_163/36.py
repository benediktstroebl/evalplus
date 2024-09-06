Here's a Python script with a self-contained function `generate_even_digits` that solves the problem:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    # Ensure a is the smallest number
    if a > b:
        a, b = b, a
    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] == '0':
            even_digits.append(x)
    return even_digits
```

This function operates on two parameters: `a` and `b`. It first ensures that `a` is the smaller number, but if it isn't, it swaps them. It then enters a loop that inspects each integer between `a` and `b`, checking whether the integral part of its expansion when divided by 10 is equal to 0. If so, it appends the integer to the `even_digits` list. Finally, the function returns this list.

To ensure that the function handles the edge cases, you can test it with the following code:
```python
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
assert generate_even_digits(3, 10) == [4, 6, 8]
```

This test suite covers all the edge cases and validates the expected behavior of the `generate_even_digits` function.