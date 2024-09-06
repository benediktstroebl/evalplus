```python
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
```
This Python script defines a function called `circular_shift` which takes two parameters, `x` and `shift`. This function manipulates the decimal representation of the integer `x` by performing a circular right shift on its digits. This shift is quantified by the `shift` parameter. If the `shift` value is greater than the length of the decimal representation of `x`, the function performs a simple reversal of this representation.

Here is an example usage of the function:
```python
# Define an integer value for x and a shift value
x = 12
shift = 2

# Call the circular_shift function with the defined values
result = circular_shift(x, shift)

# Print the result
print(result)
```
This will print the result, `12`, to the console. In this example, the shift value is 2, which is less than the number of digits in `x`. So, the function shifts the digits of `x` right by 2, and the result is the string `'12'`, which is the original number with the digits shifted.

Here is another example to demonstrate the function's behavior:
```python
# Define an integer value for x and a shift value
x = 12
shift = 3

# Call the circular_shift function with the defined values
result = circular_shift(x, shift)

# Print the result
print(result)
```
This will also print the result, `21`, to the console. In this case, the shift value is 3, which is greater than the number of digits in `x`. So, the function reverses the digits of `x` and shifts them to the left by 3, and the result is the string `'21'`, which is the original number with the digits reversed and shifted. 

This function is versatile and useful for manipulating numbers represented in base 10 and could be used in a variety of applications involving number shifting in a circular manner.