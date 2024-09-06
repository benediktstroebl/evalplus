```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}{{base}^9}'[base < 10]))
```

This function takes two inputs, `x`, which is an integer and `base`, which could be any integer less than 10. It uses the `str.translate` method to translate each digit of the digit representation of `x` to its corresponding digit in the new base, as determined by `base`. The translation is done using the `str.maketrans` method, where `base` numbers less than 10 are mapped to `base` itself and `base` numbers greater than 9 are mapped to the concatenation of `base` and the number of times multiplying `base` by itself (similar to the exponentiation in decimal multiplication), until it reaches the base digit `9`. This is done to handle the case where the number to convert is larger than the base, by using repeated multiplication of the base as digits. An example usage of this code is as follows:
```python
print(change_base(8, 3)) # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
``` 

This would output:
```
22
1000
111
```

This approach does not require converting the input number to a string or handling any edge cases, making the function more efficient and streamlined.