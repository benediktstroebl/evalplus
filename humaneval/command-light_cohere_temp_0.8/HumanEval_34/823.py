```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [-None, float('inf')] and seen.add(x)]
```
This code defines a function called unique that takes in a list l and returns a new list containing only the unique elements in l. It utilizes the unique() method with the set as seen to keep track of elements already seen in l. The unique function works by converting each element in the list to a boolean value, which is either the element itself or the negative of infinity. It then adds the unique elements to the seen set and converts them back to regular values.