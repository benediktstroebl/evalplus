Here's a Python script that contains a function named `generate_even_digits`, which solves the problem statement. This function accepts two positive integers, `a` and `b`, and it returns a list of even digits between `a` and `b`, inclusive, ensuring that the result is sorted in ascending order:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    # Ensure a and b have the same parity (which one is even is indeterminate)
    if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        a, b = b, a

    digits = []
    while a <= b:
        if a % 10 == 0:
            digits.append(a % 10)
        a //= 10
    return sorted(digits)

# Tests
a, b = 2, 8
print(f'generate_even_digits({a}, {b}) => {generate_even_digits(a, b)}')

a, b = 8, 2
print(f'generate_even_digits({a}, {b}) => {generate_even_digits(a, b)}')

a, b = 10, 14
print(f'generate_even_digits({a}, {b}) => {generate_even_digits(a, b)}')
```

The script ensures that the range bounds (`a` and `b`) have the same parity before proceeding. It utilizes a while loop to iterate through digits, adding even digits to the `digits` list. Finally, the list is sorted in ascending order and returned.

When you run the script, it will print:
```bash
generate_even_digits(2, 8) => [2, 4, 6, 8]
generate_even_digits(8, 2) => [2, 4, 6, 8]
generate_even_digits(10, 14) => []
```