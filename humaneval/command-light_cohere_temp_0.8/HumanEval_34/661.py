```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result
```
This code defines a function unique that takes a list lst as input and returns a new list containing unique elements from the input list. The function uses a set seen to keep track of elements that have already been seen, and it iterates through the input list, adding elements to the seen set if they are not already present. Finally, the function returns the unique elements of the list and returns them in the result list.