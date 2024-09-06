```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, (int, float)) or not base.isdigit():
        raise ValueError("Invalid arguments. Input and base should be integers")
    if base > 0 and base <= 36:
        return f"{x: {base}}"
    else:
        raise ValueError("Invalid base. Input base is Invalid base value.")
    return ""
``` 
This function is designed to convert a number to a string representation using a specified numerical base. The function performs input validation to ensure that the base is a positive integer within the valid range of base numbers (10 to 36). The function then uses a format specifier to properly convert the number to the desired base.