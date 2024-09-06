```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    :param x: The number to be converted
    :param base: The base to which the number is converted to
    :return: The converted string representation
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base")
    return format(x, base)

# Unit tests
test_change_base = []
test_change_base.append([['8', '2', '7', '10', 'a', 'b', 'c', 'd'])

test_change_base.append(
    {"input": 8, "base": 3, "expected": '22'},
    {"input": 8, "base": 2, "expected": '128'},
    {"input": 8, "base": 2, "expected": '1000'},
 {"input": 7, "base": 2, "expected": '111'},
 {"input": "10", "base": 2, "expected": '102'},
 {"input": "a", "base": 2, "expected": '2'},
 {"input": "b", "base": 2, "expected": '22'}

test_change_base.run(
    [('input', '8', 'base', 3, 'expected'),
    ('input', '8', 'base', 2, 'expected'),
    ('input', '7', 'base', 2, 'expected'),
    ('input', '10', 'base', 2, 'expected'),
    ('input', 'a', 'base', 2, 'expected'),
    ('input', 'b', 'base', 2, 'expected')]

if __name__ == "__main__":
    import pytest
    pytest.main()
```
This code defines a function change_base that takes an integer x and a base b as input, and returns the string representation of x in the base b. The function is tested by the built-in function unittest_main, which will run all the test cases and report the results.