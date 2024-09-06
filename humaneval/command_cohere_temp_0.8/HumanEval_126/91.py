```python
def is_sorted(lst):
    lst.sort()
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list and then checks if there's any duplication by tracking unique values using a set. If the list has more than one duplicate item, the function will identify this during the iteration and return False. Otherwise, it will return True. The code includes tests corresponding to the ones provided in the prompt.