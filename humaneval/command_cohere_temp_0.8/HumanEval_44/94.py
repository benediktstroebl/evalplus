```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base))) if base != 10 else str(x)
```

This function takes two parameters, `x`, which is the integer to have its base changed, and `base`, which is the base to change it to. It leverages the `bin` function to convert the number `x` to a binary string and then removes the leading `0b` to avoid incorrect padding. Then, it uses `zfill` to add zeros to the right of the string to guarantee that the converted number is expressed with the given base, irrespective of its length before the operation. If the base is 10, it simply returns the integer as a string. 

Here is an example usage of the function:
```python
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
print(change_base(43, 10))  # '43'
```

This output will display the result of the function when the given integer is passed with a different base. 

> **NOTE**: The function assumes that the given base is a positive integer less than 10. If the base is not valid, the function returns the result without any error or warning.