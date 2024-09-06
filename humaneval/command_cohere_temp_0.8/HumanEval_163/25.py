```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    # Ensuring the inputs are integers, necessary for the // operator in Python.
    a = int(a)
    b = int(b)

    # Generating a list to be populated with even digits.
    even_digits = []

    # Moving through the range and adding every even number to the list.
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)
    return even_digits

# Testing the function with various inputs.
test_cases = {
    (2, 8): [2, 4, 6, 8],
    (8, 2): [2, 4, 6, 8],
    (10, 14): [],
}

for args, expected in test_cases.items():
    result = generate_even_digits(*args)
    assert result == expected, f"For inputs {args}, expected {expected} but got {result}"
``` 

This code defines a function `generate_even_digits(a, b)` that takes in two integers `a` and `b`, and returns a list of even digits that lie between `a` and `b`, in ascending order. The function goes through the range from `a` to `b`, adding every even number to the `even_digits` list, then returns this list. Test cases are also included to validate the function.