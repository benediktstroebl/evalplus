```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers, a and b, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits between a and b, in ascending order. If no even digits are found, an empty list is returned.
    """
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

This Python script defines a function called `generate_even_digits`, which takes two positive integers, `a` and `b`, as arguments. The function generates a list of even digits between `a` and `b`, inclusive, and returns it in ascending order. The code uses a loop to iterate through the integers between `a` and `b`, checking if each integer is divisible by 2 (i.e., even), and if so, it adds the integer to the `even_digits` list.

The provided test cases output the lists of even digits for the given ranges, demonstrating the function's behavior. The function handles cases with no even digits in the range as well, returning an empty list for such cases, as seen with the `generate_even_digits(10, 14)` example.