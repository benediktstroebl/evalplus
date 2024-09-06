```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    if isinstance(a, int) and isinstance(b, int):
        compare_result = max(a, b)
    elif isinstance(a, float) and isinstance(b, (int, float)):
        compare_result = max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        compare_result = max(a.strip('.,'), b.strip('.,'))
    if compare_result is None:
        return None
    elif isinstance(compare_result, str):
        return compare_result
    else:
        return compare_result
```

The solution uses a logical statement to first identify the types of the input variables, then return the maximum value between the variables as long as they are of the same type. In the case where both values are strings, it uses the strip method to remove trailing `.,` and compares the string values normally. If the value is None, it returns None. You can test this code snippet by calling the function with different arguments to ensure its correctness.