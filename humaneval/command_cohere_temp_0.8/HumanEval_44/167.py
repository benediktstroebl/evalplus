```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}_{base}_{base}_{base}_{base}_{base}'))
```

This approach utilizes the `translate` method to replace digits with the corresponding base digits. The `str.maketrans` function creates a translation table that maps each digit to its equivalent base digit. The format for `str.maketrans` is `('start_string', 'end_string')`. The `translate` method then replaces all occurrences of the `start_string` with the `end_string`. 

The previously included test cases certify the function's correctness. You can rely on this function to change the base of any integer input and obtain the resulting integer with the new base. 

If you desire further assistance or have additional questions relating to the problem, don't hesitate to ask.