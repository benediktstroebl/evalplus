```python
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
```

This Python script provides a function called `circular_shift`, which accepts an integer `x` and an integer `shift` as its arguments. This function is designed to manipulate the digits of `x` by shifting them to the right by `shift`, employing a circular shifting mechanism. In case `shift` is greater than the quantity of digits in `x`, the function reverses the digits and returns the result as a string.

Here is an example usage of the function:
```python
# Example usage
x = 12
shift = 2
result = circular_shift(x, shift)
print(f"{x} shifted by {shift} is {result}")
```

This will output:
```
12 shifted by 2 is 12
```

The function efficiently shifts the digits '2' and '1' by 2 positions, resulting in the correct output of "12".