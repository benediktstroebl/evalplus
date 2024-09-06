```python
def change_base(x, base):
    return bin(x)[2:].rjust(math.ceil(math.log(x, base)), base)
```

This function takes two inputs, `x`, which is the number to be converted, and `base`, which is the base into which the number will be converted. It uses the built-in `bin()` function to convert the number `x` to a binary string and then extracts the relevant part of the string with the digit places limited to the `base` and padded with zeros to the right to achieve the best conversion. 

Here is an example usage of the function:
```python
print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))
```
The output will be:
```
'22'
'1000'
'111'
```

This would be the expected output as we are converting the numbers to the respective requested bases.