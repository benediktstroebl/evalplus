```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number to the specified base.
    Args: 
        - x (input number), 
        - base (desired base for the output string)
        
    Returns: 
        string representation of x in the specified base
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
        
    res = []
    while x > 0:
        digit = x % base
        res.append(digit)
        x // base
    return ''.join(''.join(res))

x = 8
base = 2
result = change_base(x, base)
print(result)

x = 7
base = 3
result = change_base(x, base)
print(result)

x = -3
base = 12
result = change_base(x, base)
print(result)
```
The function `change_base` in this Python script accepts two arguments: `x`, which is the input number to be transformed, and `base`, which is the base for the output string. The function initializes an empty list called `res` and then enters a loop, adding the appropriate digit to `res` from the input number `x` modulo `base` each time the loop iterates. The function then combines all of the digits in `res` into a single string and returns the string as the output.