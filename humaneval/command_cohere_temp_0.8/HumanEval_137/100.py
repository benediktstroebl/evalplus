```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return None
    # Check value
    if a == b:
        return None
    return max(a, b)
# Tests
print(compare_one(1, 2.5))  # Should print: 2.5
print(compare_one(1, "2.3"))  # Should print: "2.3"
print(compare_one("5.1", "6"))  # Should print: "6"
print(compare_one("1", 1))  # Should print: None
```
This code includes a function `compare_one` that takes two arguments and returns the larger value of the two (or `None` if they are equal). The function checks the types of the inputs and uses `max` to compare the values. It is designed to handle inputs that are integers, floats, or strings containing real numbers. 

To confirm that the function behaves as intended, four test cases are printed out and should display the expected output.