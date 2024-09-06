```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number x to base base.
    Args:
        x: number to be converted
        base: base to which the number is converted to a string
    Returns:
        string representation of x in base base
    """
    if x < 0 or base < 0:
        raise ValueError("Number is negative or invalid base")
    return format(x, f"{base}"),

def test_change_base():
    try:
        print(change_base(8, 3))
        print(change_base(-5, 2))
        print(change_base(5, 1))
        print(change_base(0, 2))
        print(change_base(-3, 5))
    except ValueError as e:
        print(e)
```
This code defines a function called `change_base` that converts a given number to a string representation in a specified base. The function uses the format() method from the built-in `datetime` module, which is suitable for representing numbers in different bases. The `test_change_base` function tests this `change_base` function by passing various test cases and checks if the function raises a `ValueError` exception or not.