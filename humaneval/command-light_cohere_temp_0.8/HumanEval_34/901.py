```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not              ]            
```  A list comprehension is used in this function to filter out duplicate elements from the input list "lst" The element is added to the "seen" set using the "not in" operator if it is not previously seen and if it is not in the set. This makes sure that we only add items to the set once and every element in the list is unique.