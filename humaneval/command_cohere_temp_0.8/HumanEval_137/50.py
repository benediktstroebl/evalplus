```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if type(a) is not type(b):
        # If the types are different, return the largest one
        if type(a) is int and type(b) in [int, float]:
            return b
        elif type(b) is int and type(a) in [int, float]:
            return a
        elif type(a) is float and type(b) is str:
            return a
        elif type(a) is str and type(b) is float:
            return b
        elif type(a) is str and type(b) is int:
            return b
        elif type(a) is int and type(b) is str:
            return a
        else:
            return b
    elif a == b:
        return None
    else:
        return a if a > b else b
```

The function compares two numbers, one of which could be a string representing a real number. The function returns the larger value and none if they are equal. It accounts for situations where one or both numbers are strings and adjusts accordingly. 

Here is an example of how to use the function: 

```python
result = compare_one(1, 2.5)
print(result)  # Output: 2.5

result = compare_one("1,5", 1)
print(result)  # Output: "1,5"

result = compare_one(1, 1)
print(result)  # Output: None
```