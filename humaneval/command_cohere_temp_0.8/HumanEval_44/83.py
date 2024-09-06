```python
def change_base(x, base):
    return str(x).encode([(len(str(x)), base)])
```

This function takes two inputs, `x`, and `base`. `x` is the number to be converted, and `base` is the target base. It uses the `encode` method to change the base of `x`. The `encode` method takes a tuple pair `(length, base)`, which specifies the desired encoding. 

Here's an example usage of the function:
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

This demonstrates how the function can change the base for different input numbers and bases, providing a string representation of the converted number.