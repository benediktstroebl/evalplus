```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension, filtering out elements that are not greater than zero. This allows it to return a list containing only the positive numbers from the input list. 

To test this function, you can use the following code: 
 ```python
test = [-1, 2, -4, 5, 6]
desired = [2, 5, 6]
assert get_positive(test) == desired
 ``` 

Adjust the test list to validate against different scenarios and ensure the function behaves as expected. 
```