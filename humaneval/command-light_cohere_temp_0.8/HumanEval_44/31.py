Here is a Python script that meets your requirements:
```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    """ Return the suitable function.
    x = int(x)  # Convert input string x to int
    return format(x, f"{base}")]

# Unit tests
def test_change_base():
    base = 10
    x = "8"
    expected = "22"
    assert change_base(x, base) == expected

if __name__ == "__main__":
    test_change_base()
```
This script defines a function called `change_base` that converts a given number to a specified base. It then returns the a formatted string representation of the number using the specified base. The script also includes unit tests using the `test_change_base` function.