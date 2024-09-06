Here's a Python script that contains a function named `generate_even_digits`, which solves the problem in the given Markdown code block:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    # Ensure that the inputs are integers and that they fall within the valid range
    a = int(a)
    b = int(b)
    if a > b:
        return []

    # Collects all even digits between a and b into a list
    even_digits = [x for x in range(a, b + 1, 2)]
    return even_digits
```

This function takes in two positive integer parameters, `a` and `b`, and returns a list of even digits that fall between `a` and `b` in ascending order. The function ensures that the outputs are sorted in ascending order and that the inputs are valid integers within the function. I've included a brief summary of the function's behavior in the comment above the code as well.

To run tests on this function, you can call it with various argument combinations and assert that the returned values are expected. Here's an example of how you might test this function:
```python
# Testing the function with various inputs and expected outputs
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
assert generate_even_digits(3, 9) == [4, 6]
```