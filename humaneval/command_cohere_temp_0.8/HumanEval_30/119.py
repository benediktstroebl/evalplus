```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` uses a list comprehension to filter the elements of the input list `l` and returns only those elements that are greater than zero, thereby solving the problem. 

Here is an example of how to use the above function:
```python
print(get_positive([-1, 2, -4, 5, 6])) # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # [5, 3, 2, 3, 9, 123, 1]
```

The function passes the test cases as expected with the help of the list comprehension, as shown in the code sample. 
If there are any further questions or any further functionality you'd like to add, let me know!
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```