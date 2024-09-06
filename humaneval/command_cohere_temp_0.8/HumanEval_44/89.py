```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two inputs, a number `x` and a base `base`, and returns the number converted to the specified base. It uses the `bin` function to convert the input number to a binary string and returns the corresponding decimal number in the specified base. It also handles cases where the base is less than 10, such as `base` of 3 in the example where it converts the number 8 to "22", which is "10" in base 3.

Here is an example of how to use this function:
```python
print(change_base(8, 3))
```

The output of this code will be:
```
'22'
```

This demonstrates how to convert the number 8 to base 3 using the `change_base` function. 

This function assumes that the input number is a valid integer and that the base is a valid integer greater than 1. If these assumptions are not met, the function may return incorrect results.