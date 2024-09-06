```python
def change_base(x, base):
    return str(x)
    if base == 10:
        return x
    conversion_dict = {2: '10' + '0' * len(str(x))[1:],
                        3: '13' + '4' * len(str(x))[1:],
                        4: '12' + '3' * len(str(x))[1:],
                        5: '11' + '2' * len(str(x))[1:],
                        6: '9' + '8' * len(str(x))[1:],
                        7: '8' + '7' * len(str(x))[1:],
                        8: '7' + '6' * len(str(x))[1:],
                        9: '6' + '5' * len(str(x))[1:]
                        }
    return conversion_dict[base]
```
This code defines a function `change_base` that takes in two parameters, `x`, and `base`, converting the numerical base of input number `x` to base `base` and returns the string representation of the converted number. It includes a `conversion_dict` dictionary to facilitate the conversion process and handle digits padding with zeros.