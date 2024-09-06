```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_true_cases = [
        (1, 2.5, 2.5),
        (1, "2,3", "2,3"),
        ("5,1", "6", "6"),
        ("1", 1, None)
    ]

    compare_false_cases = [
        (2, 3, None),
        (2.5, "2,5", "2,5"),
        ("4", "4", None),
        ("2", 2, None)
    ]

    if type(a) is not type(b):
        if isinstance(a, str) and isinstance(b, str):
            if a.find('.') != -1 and b.find('.') != -1:
                return a if a > b else b
            elif a.find(',') != -1 and b.find(',') != -1:
                return a if a > b else b
            else:
                return a if a > b else b
        elif isinstance(a, float) or isinstance(a, int):
            return a
        else:
            return b
    else:
        return None

# Tests
def test_compare_true():
    for case in compare_true_cases:
        assert compare_one(*case) == case[2]

def test_compare_false():
    for case in compare_false_cases:
        assert compare_one(*case) == None

test_compare_true()
test_compare_false()
```

### Explanation:
1. The function `compare_one()` takes two variables `a` and `b` of any type, including integer, float, or string types. 

2. The function compares the types of `a` and `b` (`if type(a) is not type(b)`). 

3. If the types are different, the function performs the following steps: 
    - If both `a` and `b` are strings, it checks whether the strings contain a comma or period. If so, it compares the decimal points and returns the string with the largest decimal point. 
    - If one variable is a string and the other is a number (integer or float), it returns the number. 

4. If the types are the same (or equivalent), it returns `None`. 

5. The function includes test suites, `test_compare_true()` and `test_compare_false()`. These test suites contain test cases that verify the function returns the correct values for various input combinations. 

6. The script runs the tests suites using the `test_compare_true()` and `test_compare_false()` functions.