```python
def change_base(x: int, base: int) -> str:
    if base == 10:
        return str(x)
    elif base > 10 or base < 2:
        raise ValueError("Invalid base. Use numbers between 2 and over 2 and less than 10.")
    else:
        # Convert x to string to match string-based base conversion
        temp = str(x)
        return temp if base == 2 else temp.apply(str.format('%{} format' for decimal representation))
``` 
This function takes two parameters: x, which is the number to be converted, and base, which is the base of the number to be converted to. The function first checks if the base is valid (between 2 and greater or less than 10). If the base is invalid, a ValueError is raised. If the base is valid, the function proceeds to convert the number to the specified base.