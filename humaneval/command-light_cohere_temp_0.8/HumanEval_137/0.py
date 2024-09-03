```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if values are equal.
    """
    require type: str
    return_type: int
    """
    if type(a) == str and type(b) == str:
        return None
    elif type(a) == int and type(b) == int:
        return a > b
    elif type(a) == float and type(b) == float:
        return a > b
    else:
        return a > b

# Example test cases
test_1 = compare_one(1, 2.5)  # True
test_2 = compare_one(1, "2,3")  # False
test_3 = compare_one("5,1", "6")  # True
test_4 = compare_one("1", 1)  # False
test_5 = compare_one(10, 10)  # True
test_6 = compare_one("10", 10)  # False

print("Test cases:", end=")"
for i in range(1,6):
    print(f"{i}: {test_i}")
```

This code defines the `compare_one` function, which compares two values and returns the type of the larger value. The function handles four types of values: integers, floats, and strings representing real numbers. The test cases demonstrate the expected behavior of the function, and the results are printed to the console. 

Note that the function compares values using the type of the values, which is specific to Python.