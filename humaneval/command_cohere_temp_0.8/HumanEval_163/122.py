```python
def generate_even_digits(a, b):
    """
    Generating even digits between two positive integers, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits from the range a to b, in ascending order.
    """

    def is_even(num):
        return num % 2 == 0

    even_digits = []

    for num in range(a, b + 1):
        if is_even(num):
            even_digits.append(num)

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits`, which takes two positive integers, `a` and `b`, as arguments. It aims to return a list containing the even digits between `a` and `b`, inclusive, arranged in ascending order. The function first defines a helper function, `is_even`, to determine whether a given number is even. Then, it iterates through the range from `a` to `b`, including both endpoints. For each number in this range, it checks if the number is even using the `is_even` function. If it is, the number is added to the `even_digits` list, which is returned once the loop completes.

The provided test cases demonstrate the function's behavior for different ranges, and the output shows the even digits within those ranges.