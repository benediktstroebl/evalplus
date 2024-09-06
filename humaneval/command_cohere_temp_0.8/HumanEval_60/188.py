```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This script defines the `sum_to_n` function, which calculates the sum of the first `n` integers using the formula for the sum of the first `n` natural numbers. The function takes an `int` argument `n` and returns an `int` value.

The `assert` statements are used to validate the function against expected results for scenarios where `sum_to_n` is called with different values of `n`. 

To execute the code, you can copy and paste it into a Python environment or script file and run it. Once executed, the script will output the results of the function calls, and the `assert` statements will validate that the function's behavior aligns with the expected outcome.  This approach allows the code to be executed as a self-contained unit, providing a straightforward way to validate and use the functionality it encapsulates.  If you face any issues executing the code or have any questions, feel free to ask!