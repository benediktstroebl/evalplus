```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not ]

# Test the function with various lists
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
print(unique([7, 11, 13, 15, 7, 8, 9]))
print(unique([20, 18, 19, 23, 10, 35, 50, 45, 65]))
print(unique([]))
print(unique([["a", "apple", "banana", "cat"]))
```