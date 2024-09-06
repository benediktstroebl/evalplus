```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function called `get_positive` that takes a list as an input parameter. It uses a list comprehension to filter out only the elements that are greater than zero from the input list, resulting in a new list that contains only positive numbers. 

The function is designed to work with any list that may contain positive or negative numbers and it efficiently separates the positive numbers from the rest. 

You can use this function to obtain a list of positive numbers from a given list by calling it with the input list as an argument, like this:
```python
result = get_positive([-1, 2, -4, 5, 6])
print(result)  # Output: [2, 5, 6]
``` 

Or in the case where the list contains a mix of positive and negative numbers along with other numeric values:
```python
result = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(result)  # Output: [5, 3, 2, 3, 9, 123, 1]
``` 

You can also test the function with different input lists to verify its behavior.