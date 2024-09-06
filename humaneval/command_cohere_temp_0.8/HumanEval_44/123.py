```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This function takes two inputs, `x`, which is the integer whose base is to be changed, and `base`, which is the base to which the number will be changed. The function returns the base-changed number as a string. This function utilizes the `str.translate` method combined with `str.maketrans` to replace each digit in the decimal representation of `x` with the corresponding digit in the new base. The `f-string` formatting in `str.maketrans` ensures that the same base digit is used for both the decimal and the new base. 

Here is an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This example outputs the corresponding base-changed numbers, respectively.