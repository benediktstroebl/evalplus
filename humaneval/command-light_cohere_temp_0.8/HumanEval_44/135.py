```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of input number x to base base.
    Return string representation after conversion
   
    base numbers less than 2 raise ValueError
    """
    if base < 2:
        raise ValueError("base must be > 2")
    return '{:0>{base}'.format(x).
    return '{:0}{base}'.format(x)

x = 8
y = 3
z = 1
result_x = change_base(x, y)
result_y = change_base(y, x)
result_z = change_base(z, y)

print(f"x: {result_x}")
print(f"y: {result_y}")
print(f"z: {result_z}")
```
The code defines a function `change_base` that converts a number to a given base. It uses base numbers less than 2, raising a ValueError for invalid base inputs. The code then applies this function to three test cases and prints the results.