Here's a self-contained Python function that solves the problem of finding unique elements in a list:
```python
def unique(l: list) -> list:
    seen = set()
    result = []
    for num in l:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theunique(result)
    return result
```
This function uses a set to keep track of seen elements and a new list to store unique elements. It iterates through elements from the list, and adds elements to the set and the unique list as it goes. The function returns the unique list.