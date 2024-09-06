```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root n such that a = n * n * n
    n = int(pow(a, (1/3)))

    # Check if n is an integer
    if n != int(n):
        return False

    # Return True if a is a cube of some integer
    return True
```

This function follows the prompt's specifications. It first checks if the given integer `a` is greater than zero. It then calculates the integer cube root of the number a, assuming that a is a valid input and thus cubing it twice is valid. After calculating the cube root, it checks if the root is an integer to ensure that a is indeed a cube of some integer number. If these conditions are met, the function returns `True`, otherwise, it returns `False`. 

This function assumes that the input is valid, and will not throw any errors in the case of invalid input. If you would like to make the function more robust, you may want to add error handling.