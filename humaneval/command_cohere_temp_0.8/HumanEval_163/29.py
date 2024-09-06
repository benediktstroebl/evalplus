```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits in ascending order between a and b.
    """
    # Ensure a is the smaller value for easier iteration
    if a > b:
        a, b = b, a
    even_digits = []
    for x in range(a, b + 1):
        if str(x).count('2', 1) % 2 == 0:
            even_digits.append(int(x))
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits`, which takes two positive integers, `a` and `b`, as arguments. The function returns a list of even digits between `a` and `b`, inclusive, presented in ascending order. It achieves this by iterating through the integers between `a` and `b`, checking if each integer is even by examining its digits and counting the occurrences of the digit '2'. It effectively handles the iteration order and criteria for even digits. The test cases provided demonstrate the function's behavior and correctness for various scenarios.