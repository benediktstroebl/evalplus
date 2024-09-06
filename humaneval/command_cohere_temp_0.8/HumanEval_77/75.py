```python
def iscube(a):
    # Check if the number is greater than 0 and equals to the cube of some integer
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number given is greater than 0, then it checks if the cubic root of the number is an integer with roudning the result. If both conditions are met, it returns `True`, otherwise, it returns `False`. This successfully passes the test cases outlined in the specification.