```python
def iscube(a):
    # Check if the number is a perfect cube
    return a ** (1/3) == int(a ** (1/3))
```

This function simplifies the problem by directly checking if the number can be cubed without any remainder. It also doesn't require the use of the `math` module. 

This solution assumes that the input is always valid, as per the prompt's instructions. If you're working with invalid inputs, you might need to add a validation check to ensure that the input is a valid integer.