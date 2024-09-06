Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists, to filter out all positive numbers from the input list and returns them. 

You can use the function like this:
```python
print(get_positive([-1, 2, -4, 5, 6])) # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # [5, 3, 2, 3, 9, 123, 1]
``` 
The function will return the list of all positive numbers included in the input list, regardless of the size of the input list and the value of the positive numbers.