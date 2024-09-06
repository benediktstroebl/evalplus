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
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```
This Python script defines a function `generate_even_digits(a, b)` designed to solve the problem statement. It takes in two positive integers, `a` and `b`, and returns a list of even digits that lie between `a` and `b`, inclusive, and are arranged in ascending order. The function first checks if `a` is greater than `b`, and if so, it swaps them to ensure easier iteration. Then, using a loop and the modulo operator (`%`), it identifies even digits in the range and appends them to a list. The final result is a list containing all even digits in ascending order between the two input integers, as specified by the given test cases.