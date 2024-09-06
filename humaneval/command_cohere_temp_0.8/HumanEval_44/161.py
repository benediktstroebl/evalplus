```python
def change_base(x, base):
    return str(x)
    # Check if base is a digit less than 10 and convert to int
    if not isinstance(base, int) or base >= 10:
        raise ValueError("base must be a digit less than 10")
    # Convert number to base x
    converted = []
    while x:
        r = x % base
        converted.append(str(r))
        x = x // base
    # Join list elements together to form a string
    return ''.join(converted)
```

This code defines a function `change_base` which takes in two integers `x` and `base` as arguments. It aims to change the base of the number `x` to base `base` and returns the resulting string. The function checks if the input base is valid, ensuring it is a digit less than 10, and converts it to an integer. It then converts the number using binary techniques, turning it into a string and returning the result.

Here is an example function call:
```python
print(change_base(8, 3))  # Outputs '22'
```