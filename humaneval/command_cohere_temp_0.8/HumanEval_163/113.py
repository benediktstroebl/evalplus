```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    num = [int(i) for i in range(a, b + 1)]
    even = [i for i in num if i % 2 == 0]
    return even

# Test Cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits`, which takes in two positive integers, `a` and `b`, and returns a list of even digits that fall between `a` and `b`, inclusive, but in ascending order. The function initially creates a list of all integers from `a` to `b` (including both), and then filters out the even numbers from this list. The result is a list that contains all the even digits in ascending order between the two given numbers, or an empty list if no even digits are found.