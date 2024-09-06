```python
def change_base(x: int, base: int) -> str:
    """Change the base of integer x to base base"""
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    # Use str.format to ensure the format a number in desired base
    return format(x, base)

# Unit tests
test_change_base = []
test_change_base.append([lambda x, base:
    change_base(x, base).assertEqual(f"{x:d} in base {base}", f"{x:d}"))
test_change_base.append(lambda x, base:
    change_base(x, 10) == "100000000000" and \
            change_base(x, 2) == "22" and \
            change_base(x, 16) == "16" and \
            change_base(x, 32) == "1"
test_change_base.append(lambda x, base:
    change_base(x, 0) == "" and \
            change_base(x, 57) == ""
test_change_base.test_change_base()

``` 
This script defines a function `change_base` that converts a number to a specified base. It also includes unit tests to ensure the function is working correctly with various inputs and base numbers.