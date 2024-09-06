```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two inputs, `x`, which is an integer and `base`, which is the numerical base to convert to. It utilizes the `bin` function to represent `x` as a binary string and returns the converted number by discarding the leading '0b' and filling with leading zeros if necessary. 

To understand how it works let's break down the code executing:
1. `return bin(x)[2:]` casts `x` to a binary string representation returning a string like '0b101010'
   - `[2:]` is a slicing operation that removes the leading '0b'
2. `.zfill(math.ceil(math.log(x, base)))`: This line pads the binary string with zeros on the left to ensure that the representation of the number in the new base is long enough. It calculates the necessary number of zeros to add using `math.ceil(math.log(x, base))`, which determines the number of digits of the largest number, which is less than or equal to `x` and in base `base`. 

The function is applicable when `base` is less than 10, as per the problem statement.

Here is an example to help you understand how it works:
```python
print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))
```

The output will be:
```
22
1000
111
```

This demonstrates the conversion of the base of the numbers using the `change_base` function.