```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root n such that a = n * n * n
    n = int(pow(a ** (1/3)), 3)

    # Check if n * n * n equals a
    return n * n * n == a
```

This function follows the steps outlined in the problem. It first checks if the given number `a` is greater than 0. If `a` is not greater than zero, it returns False, as there cannot be a cube of a number that is smaller than or equal to zero. Then, it calculates the integer cube root of `a` (`n`) by raising `a` to the power of 1/3 and then converting this float to an integer. Finally, it checks if `n * n * n` equals `a` and returns this comparison result. 

The function returns `True` if `a` is a cube of some integer and `False` otherwise. Also, the code assumes that the input is always valid, as stated in the problem. 

This approach assumes that the input will always be a valid integer, as taking the integer cube root of a non-integer will result in a complex number. However, if you have a specific use case in mind that might involve non-integer inputs, you may need to adjust the approach accordingly.