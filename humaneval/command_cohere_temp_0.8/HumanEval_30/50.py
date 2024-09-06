```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` takes a list (`l`) as an argument and returns a new list that contains only the positive integers from the original list. 

If the list contains non-integer elements or negative numbers, those elements will be excluded from the resultant list. 

The function solves the problem using a concise list comprehension, filtered by the condition `x > 0`. 

This solution is just one of many ways to solve this problem, but it is straightforward and should work well for the specified test cases.