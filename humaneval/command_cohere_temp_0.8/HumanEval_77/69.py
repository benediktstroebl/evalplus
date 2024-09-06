```python
def iscube(a):
    # Check if the number is greater than 0 and equals to val^3
    return a > 0 and a ** 3 == int(a ** 3)
```

This function simply checks if the number is greater than 0 and evaluates the cube of the integer `val` using the `**` operator. Then it compares the result to the original integer `val` using the `==` operator. If the result is an integer, it returns `True`. If not, it returns `False`.

This approach takes advantage of the fact that the cube of any integer is always positive and the fact that the floor division of an integer by another integer always yields an integer. 

Please note that this assumes that the input is always valid as stated in the assumption in the prompt. If you were to deal with invalid input, you may need to add a validation step to your code.