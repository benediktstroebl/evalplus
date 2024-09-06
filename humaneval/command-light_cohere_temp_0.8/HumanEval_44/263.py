```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base.
    Return the string representation.
    base numbers are  are 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 4)
    TraceError
    """
    return '{:02}'.format(x, base)

def test_change_base():
    base_numbers = [10, 2, 7, 85, 420]
    for base, expected in zip([2, 10], base_numbers):
        actual = change_base(20, base)
        assert actual == expected, f"For base {base}, expected {expected}, but got {actual}"

if __name__ == "__main__":
    test_change_base()
```
The code defines a function `change_base` that converts a number to a given base. It then has a test function `test_change_base` which contains tests that validate the correctness of the `change_base` function.