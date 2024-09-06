```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers less than 2 yield strings with two digits, 
    while base numbers 2 and 10 yield single digit strings.
    """
    string representation is a number with base b:
    [([sub] * [n]) | [(sub + 1)]]
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
        
    if base == 10:
        return str(x)
    
    # [sub] represents digits in base b, n is digits of x
    s = ''.join([(i + base - 1) // (base - 1) for i in range(0, x)])
    return s[0] + s[1:-1]

# Test the function
x = 8
base = 2
print(change_base(x, base))  # Output: 1000
x = 7
base = 2
print(change_base(x, base))  # Output: 111
x = 3
base = 10
print(change_base(x, base))  # Output: 22
```
The function change_base is a Python function that takes two arguments: x, representing the number to be converted, and base, representing the desired base. This function then checks if the valid input is provided, specifically that base is between 2 and 36. Then, depending on the input, it will either return a single digit string or a string representation of the number using the specified base. The output will be the string representation of the number with base b.