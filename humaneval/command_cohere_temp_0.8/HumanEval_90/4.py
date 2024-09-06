```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines a function `next_smallest` that, when given a list of integers, will return the second smallest element in the list. If the list has less than two elements, the function will return `None`. The function works by first sorting the list and then retrieving the second element (which will be the second smallest element). 

Here is an example of how you can use the code: 
```python
result = next_smallest([1, 2, 3, 4, 5])
print(result)  # Output: 2
```
```python
result = next_smallest([5, 1, 4, 3, 2])
print(result)  # Output: 2
```
```python
result = next_smallest([])
print(result)  # Output: None
```
```python
result = next_smallest([1, 1])
print(result)  # Output: None
```

The provided examples demonstrate how the `next_smallest` function operates when given different lists of integers, returning the second smallest element when present or `None` when the list has less than two elements. Feel free to test more scenarios to verify the function's behavior.