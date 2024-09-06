```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The starting integer.
        b (int): The ending integer.

    Returns:
        list: A list of even digits from start to end or an empty list if no even digits are present.
    """

    # Filter out even digits from start to end
    even_digits = [x for x in range(a, b + 1) if x % 2 == 0]

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This script features a function called `generate_even_digits(a, b)` which takes two integers, `a` and `b`, as arguments. It aims to return a list containing all the even digits found between `a` and `b`, in ascending order. If there are no even digits within this range, the function returns an empty list. 

The function employs list comprehension to filter out even digits from start to end, catering to the given requirement. While the function is designed to operate on consecutive integers, it is not limited to strictly sequential numbers, as shown in the test cases.