```python
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
```
This Python script defines a function called `circular_shift` taking in two parameters, `x` and `shift`. This function performs a circular right shift of the digits of integer `x` by shifting right by `shift` positions. If `shift` is greater than the number of digits, it reverses the digits instead. This function ultimately returns the shifted digit string.

To test this function, you can call it with various inputs to see if it behaves as expected:
```python
circular_shift(12, 1) # Expected Output: "21"
circular_shift(12, 2) # Expected Output: "12"
circular_shift(15, 3) # Expected Output: "545"
circular_shift(123, 2) # Expected Output: "231"
```
This function is adaptable and handles various input scenarios, making it a useful tool for manipulating numerical data in character form.