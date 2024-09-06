```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in [0,None]]

#Test case 1: [5, 3, 5, 2, 3, 3, 9, 0, 123] -> [0, 2, 3, 5, 9, 123]

#Test case 2: [] -> []

#Test case 3: ([1,2]) -> [1,2]

#Test case 4: ([1,2,3]) -> [1,2,3]

#Test case 5: ([1,2], [3,4]) -> [1,2], [3,4]

#Test case 6: (1,2,3,4,5,6) -> [1,2,3,4,5,6]
```