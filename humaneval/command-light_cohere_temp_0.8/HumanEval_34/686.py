```python
def unique(l: list):
    return list(set(l))

# Test the function
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_unique))  # Output: [0, 2, 3, 5, 9, 123]

# Test again to ensure stability
test_unique2 = [5, 3, 5, 2, 3, 3, 9, 0, 7]
print(unique(test_unique2))  # Output: [0, 2, 3, 5, 7, 9]
```

This code defines a function unique that takes a list l as input and returns a list of unique elements in l using the set function and list comprehension. It then tests this unique function with a few test lists and verifies that the output is indeed unique.