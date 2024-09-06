```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns a string representation after conversion.
    base numbers 10.
    """ Returns format of from a custom string.
    x = int(input())
    base = int(input())
    if x < 0 or base < 2:
        raise ValueError("Invalid input values.")
    return f"{x:d}_{base:d}"

# Unit tests
test_change_base = []
test_change_base.push((-10, 10))
test_change_base.push(10, 10)
test_change_base.push(10, 20)
test_change_base.push(10, 2)
test_change_base.push(11, 2)
test_change_base.push(10, 1)
test_change_base.push(20, 2)
test_change_base.push(20, 1)
test_change_base.push(1, 20)

def test_function():
    for test_case in test_change_base:
        assert change_base(*test_case) == str(test_case)

test_change_base.push(20, 3)
test_change_base.push(30, 3)

# Example usage
x = 10
base = 2
result = change_base(x, base)
print(result)  # Output: "20_2"
``` 
This Python code defines a function `change_base` that converts a number to a specified base. It uses a `test_change_base` module to run unit tests for the `change_base` function. The tests ensure that the function handles invalid inputs correctly and provides the expected output. The `test_change_base` module contains a list of test cases, including both base numbers and the input numbers to be converted. The `change_base` function takes a number `x` and a base `base` as input and returns the converted string representation of `x` in the specified base. The example usage demonstrates the use of the `change_base` function by converting the number 10 to base 2 and then printing the result.