```python
def circular_shift(x, shift):
    s = str(x)
    digits = list(s)
    if shift > len(s):
        shift = shift % len(s) 
    digits = digits[shift:] + digits[:shift]
    return ''.join(digits)
```

The function first converts the integer `x` to a string, and then converts that string into a list of digits. It performs a circular shift of the digits, meaning it shifts the digits to the right by `shift`, and then back to the left. If `shift` is greater than the length of the digit list, it performs a modulo operation to only shift by the relevant digits. Finally, it joins the list of digits back into a string and returns the result. 

The base case tests in the original prompt demonstrate its behavior for shifts of 1 and 2, returning '21' and '12' respectively for the input value of 12.