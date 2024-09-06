```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, (int, float)) or not base.isinstance(base):
        raise TypeError("Invalid arguments. Ensure x is base is an integer")
    if base < 2 or base > 36:
        raise ValueError("Invalid base number. Ensure the base is a between 2 and 36.")
    return format(x, base)
``` 
This function takes two parameters: x, which is the number to be converted, and base, which is the base to which the number will be converted. The function then checks that the arguments are valid, and raise appropriate errors if they are not. It then converts the string formats the number using the specified base.