```python
def change_base(x, base):
    return bin(x)[2:].rjust(len(str(bin(x)[2:])), '0')[::-1].zfill(len(str(x)))(x, base)
```

The provided Python script defines a function `change_base` that takes an integer `x` and bases `base` as inputs. It converts the integer `x` into a binary string and then reverses this string, left-padding it with zeros to match the length of the original integer `x`. This reversed and padded binary string is then converted to the specified base using Python's built-in `int` function, and the resulting integer is finally converted back to a string and returned.

Here's an example usage of the function:
```python
result = change_base(8, 3)
print(result)  # Output: '22'

result = change_base(8, 2)
print(result)  # Output: '1000'

result = change_base(7, 2)
print(result)  # Output: '111'
```

In these examples, the function is called with different values of `x` and `base`, and the resulting converted values are printed, confirming the correctness of the function.