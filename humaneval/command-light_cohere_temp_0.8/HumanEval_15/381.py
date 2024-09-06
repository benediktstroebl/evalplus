Here's a self-contained Python script that defines a function to create a sequence of numbers in a markdown-formatted string:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + str_sequence(n - 1) + "}" 

def str_sequence(count: int) -> str:
    return "".join() + str_sequence(count - 1) + "\n"

# Basic input validation test
def test_string_sequence(func):
    try:
        n = int(input("Enter the value for n: "))
        if n < 0:
            raise ValueError("n should be a non-negative integer")
        return func(n)
    except ValueError as e:
        print("Error:", e)
    return 

# Test the function with different inputs
test_string_sequence(string_sequence)
```
The `string_sequence` function uses recursion to create a sequence of numbers and the `str_sequence` helper function helps in building the string by adding the appropriate number of spaces. The function also includes input validation tests to ensure that the user enters a valid, non-negative integer for the `n` parameter.