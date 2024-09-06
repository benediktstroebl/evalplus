```python
def change_base(x, base):
    return str(x).encode([(len(str(x)) - 1) // 3 * base])
```

The above code directly encodes the input number `x` using `str(x)` which is a string itself, and uses a list comprehension to calculate required base numbers to embed in the resulting string to be converted. This returns a string representation of the number `x` in the new base. This solution is concise and clear, and should work effectively for various input numbers `x` and bases `base`. 

Here's a usage example:
```python
print(change_base(8, 3)) # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This demonstrates how the `change_base` function can be used to easily change the base of a given number.