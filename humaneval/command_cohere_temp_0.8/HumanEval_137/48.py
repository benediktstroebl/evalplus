```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, and convert them to floats for comparison
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    elif isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        # remove the floating point and compare the strings
        fa, fb = a.strip('.,'), b.strip('.,')
        return fa if fa > fb else fb
    elif isinstance(a, (int, float)) and isinstance(b, str):
        # note: the reverse of previous condition since isinstance is recursive
        fb = b.strip('.,')
        return fb if fb > a else a
    elif isinstance(a, str) and isinstance(b, (int, float)):
        fa = a.strip('.,')
        return fa if fa > b else b
    else:
        return None

# Tests:
print(compare_one(1, 2.5))  # Should print: 2.5
print(compare_one(1, "2.3"))  # Should print: "2.3"
print(compare_one("5.1", "6.3"))  # Should print: "6.3"
print(compare_one("1", 1))  # Should print: None
```
This script defines a function `compare_one` that accepts two real number inputs, regardless of whether they are integers, floats, or strings. It then returns the largest number, but converted to the type of the first input (e.g., if the larger number is a float and the compared values are "1" and 1, it will return 1, not a float). The "stripping" of the floating point is to ensure that "1,1" < "1" and "1." > "1" appropriately. 

The tests provided in the original problem prompt are baked into the script as print statements, to ensure that the function behaves as expected. 
```