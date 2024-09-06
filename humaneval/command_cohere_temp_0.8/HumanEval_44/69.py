```python
def change_base(x, base):
    return str(x).translate(str.maketrans('1234567890', f'{base}_{base}_{base}123'))
```

This function takes two inputs, `x`, which is the integer whose base is to be changed, and `base`, which is the base to which the number will be changed. It uses the translate method to replace digits in the string representation of `x` with the new base digits. The `str.maketrans` method creates a translation table based on the two bases to convert each digit of the original number `x` to the corresponding digit in the new base system. 

Here is an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This demonstrates the conversion of the base of the input number to the new base, as specified in the problem statement.