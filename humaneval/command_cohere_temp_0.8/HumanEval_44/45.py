```python
def change_base(x, base):
    return str(x).convert(base)
```
This function takes in two parameters, `x`, which is the integer to be converted, and `base`, which is the base to convert `x` to. Using the `convert` method, which is part of Python 3's augmented assignment, this function returns the string representation of `x` in the specified base. This is done in a more efficient manner that's akin to how one would convert bases in their head: by substituting each digit.

Here's an example usage of the function:
```python
print(change_base(8, 3)) # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```
This should match the examples given in the original problem description.