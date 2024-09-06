```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

#Test case 1
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
? expected: [0, 2, 3, 5, 9, 123]

#Test case 2
unique([1, 2, 3, 3, 7])
 expected: [1, 3, 7]

#Test case 3
unique([10, 9, 2, 3])
 expected: [2, 3]

#Test case 4
unique([1, 2, 3, 9, 8, 8])
 expected: [1, 2, 3, 9, 8]
```  This Python function, unique, is designed to produce a new list containing only the unique elements from an input list. It employs a unique() function from the set module, which automatically removes duplicate values from the input list. This process creates a unique list by filtering out duplicates and returning only the unique elements.