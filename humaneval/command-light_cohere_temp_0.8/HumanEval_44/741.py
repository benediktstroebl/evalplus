```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    :param x: int number to be converted
    :param base: new base to convert to
    :return: string representation of x in the given base
    """
    if x < 0:
        raise ValueError("Input number cannot be negative")
    return format(x, f"{base}]", int("01"))

# Example usage
x = int(input("Enter a number: "))
base = int(input("Enter a base to convert to: "))

try:
    print(change_base(x, base))
except ValueError as ve:
    print(f"Error: {ve}")
```
The provided Python code defines a function `change_base` that converts a given number x to a specified base. The base for the **number** is provided by the user as an argument. The function handles negative numbers and raises a `ValueError` exception if the input is negative. 

It then uses the `format` method to convert the number to the specified base, and returns the string representation of the number in the new base.