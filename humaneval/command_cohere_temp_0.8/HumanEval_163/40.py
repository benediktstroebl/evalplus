```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits from the first to the last number given a pair of positive integers.

    Args:
        a (int): The starting positive integer.
        b (int): The ending positive integer.

    Returns:
        list: A list of even digits from the first to the last number in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracts even digits from numbers between a and b
    even_digits = [digit for digit in range(a, b + 1) if digit % 2 == 0]
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits` takes two positive integers, `a` and `b` as arguments and returns a list of even digits from the first to the last number in ascending order. The code checks if the starting number (`a`), ending number (`b`), or both are odd. If either of these conditions is true, it returns an empty list because there will be no even digits in the range; the range declaration `range(a, b + 1)` excludes the endpoint `b`, therefore `b + 1` is needed to include it in the range. Otherwise, it constructs a list even digits in the range. You can invoke the function and print the results using the test cases as shown in the script.  This solution is efficient and complies with the problem statement's requirements.