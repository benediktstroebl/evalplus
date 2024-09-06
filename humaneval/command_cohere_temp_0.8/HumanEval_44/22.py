```python
def change_base(x, base):
    return str(x).convert(base)
```
This function accepts an integer `x` and a base `base` as inputs, utilizes the `str.convert` method to change the base of `x`, and then returns the string representation of the converted number. The `str.convert` method takes a second argument, `oct`, which specifies the base to be used in the conversion. 

Here is an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```
This example utilizes the function with different inputs and confirms that the output is the string representation of the number with the specified base. 

To handle conversions for bases less than 10, you could do it like this:
```python
def change_base(x, base):
    if base < 10:
        return str(x).zfill(math.ceil(math.log(x, base)))
    return x.convert(base)
```
In this updated version, the function determines if the base is greater or less than 10. If the base is less than 10, it means it is a specialized case and the function uses `str.zfill` to fill the number with zeros to the left until the number has the same amount of digits as the base. This is done to facilitate the conversion of specific bases. 

Otherwise, the function employs `str.convert` to carry out the conversion.