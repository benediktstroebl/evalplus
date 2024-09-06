```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base
    """
    return f"{x:>{base}"

# Tests
test_change_base = {
    "input": [8, 3, 2, 7],
    "expected": ['22', '8', 'II', 'II'],
}

test_change_base_long = {
    "input": [123, 10],
    "expected": ['1300'],
}

def test_change_base():
    for input_, expected in test_change_base.
    actual = change_base(input_, 10)
    assert actual == expected, f"Mismatch at input {input_} expected {expected}, actual {actual}"

test_change_base()
```
The code defines a function change_base that converts a number to a specified base. It also includes a set of test cases for the function's functionality, which are run using the built-in test_change_base function.