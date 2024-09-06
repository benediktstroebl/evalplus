Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list with only the positive numbers from the input list. 

If the input list `l` is defined as `[-1, 2, -4, 5, 6]`, the function will return `[2, 5, 6]`. 

And if the input list is instead ` [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`, the returned list will be `[5, 3, 2, 3, 9, 123, 1]`. 

This solution is concise and efficient, providing a useful tool for filtering positive numbers from any given list.