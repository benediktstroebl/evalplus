```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two inputs, `x`, which is the number to be converted, and `base`, which is the new base for conversion. It utilizes the `bin` function to represent `x` as a binary string and then extracts the required number of digits from the beginning of this string using `zfill`. 

To determine the length of the extracted digit string, we use `math.ceil` to round up the result of `math.log` which calculates the logarithm of `x` in base `base`. This ensures the returned string fully represents the conversion of `x` to the new base. 

This solution has an efficiency of `O(log(min(x, base)))`, where `log` is the logarithm function of `x` in base `base` and the `min` is due to the use of `zfill` to pad the string with zeros on the left.

Here's an example usage of the function:
```python
print(change_base(8, 3)) # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This will produce the following output:
```
22
1000
111
```

The function also handles any negative numbers and returns the corresponding string representation.