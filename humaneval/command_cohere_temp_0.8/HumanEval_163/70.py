```python
def generate_even_digits(a, b):
    """
    Generating even digits between two integers.
    
    Args:
    - a (int): Starting integer.
    - b (int): Ending integer.
    
    Returns:
    - list: List of even digits in ascending order.
    """
    # Ensuring a is the maximum to avoid empty list on margin-case.
    if a > b:
        a, b = b, a
    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] == '':
            even_digits.append(int(x))
    return even_digits

# Testing Module
def test_even_digits():
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == [12, 14]

# Run the tests.
test_even_digits()
```

This Python script defines a function called `generate_even_digits`, which takes two integers as input and returns a list of even digits that occur between the two integers, in ascending order. 

The function first checks if `a` is greater than `b` and swaps them if necessary to avoid an empty list on the margin case. It then iterates through integers from `a` to `b`, where `a` is included and `b` is excluded, and checks whether the digits of the integer are even. If so, the integer is added to the `even_digits` list. Finally, the function returns the `even_digits` list. 

The script also includes a test module with a single function `test_even_digits`, which tests the `generate_even_digits` function with example inputs and expected output. The `test_even_digits` function is then called to execute the tests.