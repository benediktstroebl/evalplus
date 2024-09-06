Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
The function utilizes a list comprehension, iterating through each element in the input list `l`. For each element `x`, it checks if `x` is greater than zero. If the condition is met, the element is included in the resultant list that is returned. 
The expected output of the given examples in the comment is also returned by the function, respectively: `[2, 5, 6]` and `[5, 3, 2, 3, 9, 123, 1]`.