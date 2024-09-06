```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    if a % 2 == 0 and b % 2 == 0:
        result = []
        for x in range(a, b + 1):
            if x % 2 == 0:
                result.append(x)
        return result
    else:
        return []

# Testing the function
def test_even_digits():
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == []

test_even_digits()
```

To guarantee that the produced list only contains even numbers, the function iterates through the numbers from `a` to `b` and checks if each number is divisible by 2 (i.e., even). The list is empty if there are no even numbers in the specified range.

The `test_even_digits` function serves as a test script for the `generate_even_digits` function. It verifies the function's behavior using three distinct scenarios `(2, 8), (8, 2), and (10, 14)` and ensures that the expected results are produced. Using the `assert` statement, it checks the function's output against the anticipated even digits in each case. 

The `test_even_digits` function is called at the end to execute the tests. If the function is implemented correctly, all tests will pass, and no exceptions will be thrown. If the tests fail, the script will provide details on where it failed, helping to identify and fix any issues in the function.  It is advised to use a powerful testing framework, such as `pytest` or `unittest`, for more sophisticated and organized testing procedures. To completely evaluate the behavior of the function, it is essential to execute a variety of tests covering various scenarios, edge cases, and potential errors.  If you want to learn more about testing and test methodologies, consider researching the behavior-driven development (BDD) approach and tools such as `pytest-bdd` or `behave`.