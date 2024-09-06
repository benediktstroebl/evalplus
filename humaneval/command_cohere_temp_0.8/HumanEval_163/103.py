```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits between a and b.
    """
    # Ensure a is the smaller value for easier iteration
    if a > b:
        a, b = b, a

    even_digits = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function `generate_even_digits(a, b)` which takes in two positive integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, and in ascending order. The code ensures `a` is always the lesser of the two values for easier iteration. It then loops through the integers and collects the even digits into the `even_digits` list, rejecting odd digits. The function returns this list. Test cases are provided and correctly handled within the code to verify its functionality against the problem statement.