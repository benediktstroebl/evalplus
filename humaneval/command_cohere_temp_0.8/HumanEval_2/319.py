```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(0.1) == 0.0
```

This script includes a function `truncate_number` that returns the decimal part of the given number by subtracting the closest integer to it. It also includes a test block that checks the function's output against expected values. You can use the `assert` statements to verify the function's behavior against different test cases.  Each assertion checks that the function's output matches the expected output for a specific input.  If every test passes, the function's behavior aligns with the expected behavior outlined in the original problem statement.  This would mean that the code is properly self-contained and solves the defined problem.  You can add more test cases to cover a wider range of scenarios and ensure the function's correctness better.  This approach enables developers to validate their code and demonstrate problem-solving skills in a structured format.