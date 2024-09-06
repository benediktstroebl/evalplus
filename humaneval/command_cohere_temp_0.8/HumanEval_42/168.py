Here is a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list as input and returns a list of incremented numbers by using a list comprehension with the expression `x + 1 for x in l`. 

You can test this function with the following calls:
```python
incr_list([1, 2, 3]) # [2, 3, 4]
incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

Let me know if this solution suits your needs or if you'd like me to make any adjustments to the code. I'm here to help optimize or improve the solution further if needed. Feel free to add more test cases or provide other examples to ensure the function handles all edge cases.