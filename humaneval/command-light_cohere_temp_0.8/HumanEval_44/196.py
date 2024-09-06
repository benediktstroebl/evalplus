```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Invalid input types. Input must be an string representing a number and a base number respectively.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    return str(x, base)
``` 
This function changes the base of a given number to the base of the specified base. It uses the str function to convert the number to a string. It then uses the str function to convert the string to a number with the desired base. The function raises a ValueError exception if the input types are invalid or if the base is outside the valid range.