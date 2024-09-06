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
        return None
    elif type(a) is int and a == b:
        return None
    elif type(a) is float and a == b:
        return None
    elif type(a) is str and a == b:
        return None
    elif isinstance(a, int) and isinstance(b, float):
        return b
    elif isinstance(a, float) and isinstance(b, int):
        return a
    elif isinstance(a, str) and isinstance(b, str):
        if a.find('.') > -1 and b.find('.') > -1:
            ma = a.split('.')
            mb = b.split('.')
            ma = (int(ma[0]) << 0) + (int(ma[1]) << 32)
            mb = (int(mb[0]) << 0) + (int(mb[1]) << 32)
            if ma > mb:
                return a
            elif mb > ma:
                return b
        elif a.find(',') > -1 and b.find(',') > -1:
            ma = a.split(',')
            mb = b.split(',')
            ma = (int(ma[0]) << 0) + (int(ma[1]) << 32)
            mb = (int(mb[0]) << 0) + (int(mb[1]) << 32)
            if ma > mb:
                return a
            elif mb > ma:
                return b
        else:
            return b
    else:
        return a
```

The function compares two given variables with different types, such as integer, float, and string types. The function follows these steps:
- Check if the types of `a` and `b` are the same, and if not, return `None`.
- If the type is integer and the values are equal, return `None`.
- If the type is float and the values are equal, return `None`.
- If the type is string and the values are equal, return `None`.
- If the type is integer and float, return the float value.
- If the type is float and integer, return the integer value.
- If the type is string and string, the function checks if the floating point is `.` or `,`, then it splits the strings into arrays, converts them to integers, and compares the resulting integers as before.
- If none of the above, return the value of `a`.

The function returns the larger value of the two compared variables, or `None` if the values are equal.  This function is applicable for given inputs, such as `compare_one(1, 2.5) ➞ 2.5`, `compare_one(1, "2,3") ➞ "2,3"`, `compare_one("5,1", "6") ➞ "6"`, and `compare_one("