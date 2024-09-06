```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers, a and b, inclusive.
    """
    # Ensure a is the numerically smaller value for proper iteration
    if a > b:
        a, b = b, a
    even_digits = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)
    return even_digits

# Example usage
a = 2
b = 8
result = generate_even_digits(a, b)
print(result)  # Output: [2, 4, 6, 8]
```

This Python script defines a function `generate_even_digits(a, b)` which accepts two positive integers and iterates through the digits between `a` and `b`, only adding the even digits to a result list. The function then returns this list. The code includes a demonstration of this functionality with the `print(result)` statement, producing the output `[2, 4, 6, 8]`.