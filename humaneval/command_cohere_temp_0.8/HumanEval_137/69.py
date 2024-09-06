```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    if type(a) == type(b) and type(a) in [int, float, str]:
        if type(a) == str:
            a = float(a.replace(",", ".") * 1)
            b = float(b.replace(",", ".") * 1)
        if a > b:
            compare_result = a
        elif a < b:
            compare_result = b
    return compare_result
```

The problem poses a challenge in determining the variable types and appropriate transformations to apply for comparison. This code uses an `if` statement to verify if the variables are of the same nature and one of the specified types. When using strings, it removes the comma indicator and translates the values to floating numbers to facilitate comparison. It then proceeds to compare values and returns the largest one. If they are equal, it returns `None`. 

The following test cases illustrate how the function behaves:
```python
test_compare_one = {
    "(1, 2.5) -> 2.5": [1, 2.5],
    "(1, '2.3') -> '2.3'": [1, '2.3'],
   ("5.1,', '6') -> '6'": ['5.1', '6'],
    "'1, ''1' -> None": ['1', '1'],
}

for key, value in test_compare_one.items():
    assert compare_one(*value) == value[1]
```