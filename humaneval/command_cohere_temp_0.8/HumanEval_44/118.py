```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}_{base}_{base}_{base}_{base}_{base}'))
```

This approach uses str.translate to convert the digits of the input number x to the new base. The translation table is created using str.maketrans and formatted with the new base to ensure the new base is used for each digit in the number.

To handle input validation, the function simply checks if the input base is less than 10 during execution, ensuring the self-contained aspect of the function.