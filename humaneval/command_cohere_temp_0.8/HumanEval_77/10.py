```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Check if the number is a perfect cube
    root = int(pow(a, (1/3)))
    return root ** 3 == a
```

This function checks if the number is greater than zero, and if so, it calculates the integer cube root of the number. If the cube root transformed the number to the original value, the function returns True, otherwise, it returns False.