```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some integer
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the root of the number (a ** (1/3)) is an integer with round() function, which converts the floating point result of the cube root to the nearest integer. Thus, it returns True if the number is a cube of some integer and False otherwise. 

This approach assumes that the input is always valid, as stated in the prompt. It is always a good idea to handle edge cases and validate input to ensure robustness of your code.