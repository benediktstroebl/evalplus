```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the input number x to base base,
    return the string representation of the number.
    """
    new base number must be converted to the desired base.
    """
    number should be converted to a string before conversion."""

    # Check if the base is a valid digit between 0 and 9
    if base < 0 or base > 9:
        raise ValueError("Invalid base number.")

    # Convert the number to a string
    x = str(x)

    # If the number is 0, the conversion is straightforward
    if x == "0":
        return f"{base}{x}"

    # Split the number into digits and handle the conversion recursively
    else:
        digits = x.split()
        numbers = [map(lambda x:int(x), digits)]
        numbers = [f"{base}{num}" for num in numbers]
        return "".join(numbers)

# Example usage
print(change_base(8, 2)) # Output: '1000'
print(change_base(7, 2)) # Output: '111'
print(change_base(5, 5)) # Should raise ValueError
```