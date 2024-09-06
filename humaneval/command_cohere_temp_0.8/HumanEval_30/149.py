Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists, to filter out all positive numbers from the input list `l`. It works efficiently and returns a new list that includes only the positive numbers present in the input list. 

You can use the `get_positive` function like this:
```python
print(get_positive([-1, 2, -4, 5, 6])) # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # [5, 3, 2, 3, 9, 123, 1]
```
This will output the list containing only positive numbers. Feel free to use it for your problem and customize it further if needed. Let me know if you would like me to explain any Python concepts used in this script.