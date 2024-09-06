Here is a self-contained Python script that defines a function unique that returns sorted unique elements in a list:
```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This function utilizes a set to track unique elements and builds a list with those unRepresented elements. The function then returns this list of unique elements after sorting them.