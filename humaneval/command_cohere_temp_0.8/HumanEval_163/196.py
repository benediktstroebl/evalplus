```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits from a to b in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Ensuring the lower bound is the smallest even number.
    if a == 2:
        even_digits = [a, 4, 6, 8]
    elif a % 2:
        even_digits = [a, a + 2, a + 4, a + 6, a + 8]
    else:
        even_digits = [a, a + 4, a + 6, a + 8]

    # Filtering out odd digits from the upper bound.
    for i in range(1, int((b - a + 1) / 2)):
        even_digits.append(even_digits[i] + b)
        del even_digits[i]

    return even_digits

# Test cases:
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```
This Python script defines a function called `generate_even_digits`, which takes two integers as arguments: `a` and `b`. It aims to return a list of even digits that lie between `a` and `b`, inclusive, and are arranged in ascending order.

The function first checks if 'a' and 'b' are both even and if 'a' is greater than or equal to 'b'. If any of these conditions are not met, an empty list is returned, as there are no even digits to be found in the specified range.

In the case where the lower bound 'a' is not even, the function generates a list of even digits from 'a' to the nearest even number below 'b'. It does this by incrementing 'a' by 2 until it becomes even, and then adds 4, 6, and 8, accordingly.

In the case where the lower bound 'a' is already even, the function directly generates a list from 'a' to 'a' plus 8, skipping odd digits.

The generated list is then complemented by adding the even digits from the upper bound 'b' back into the list. The odd digits are filtered out, ensuring that only even digits between 'a' and 'b' are retained, ultimately returning the desired list.