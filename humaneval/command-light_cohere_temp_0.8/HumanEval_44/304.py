```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 2)
    Traceback (most recent call last):
      File "<input>", line 3, in <module>
    AssertionError: 0 not integer()
    """
    if not_integer(x) or not isinstance(base, int):
        raise AssertionError("Input must be an integer")

    if base < 2 or base > 36:
        raise AssertionError(f"Base must be between 2 and 36 inclusive")

    return format(x, f"{base}")

def not_integer(x: int) -> bool:
    return isinstance(x, int)

def main():
    base = 10
    x = int(input("Enter a number: "))
    result = change_base(x, base)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```
This script defines a function `change_base` that converts a given number `x` to a specified base `base`. It also has two helper functions: `not_integer` to check if a given input is an integer, and `main` which acts as the driver function to run the `change_base` function with an example usage.  When use the Marathon's Auto-fill code.