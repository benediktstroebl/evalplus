Here is a self-contained Python script that defines a function unique which returns sorted unique elements in a list:
```python 
def unique(lst): 
    return list(set(sorted(lst)))

# Test cases
test_unique = [ 
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [6, 8, 7, 7],
    [5, 5, 'five']
]

for test in test_unique: 
    print(unique(test))
```
The function unique uses the set and sorted functions to remove duplicates and maintain unique elements in the list. The test cases demonstrate the