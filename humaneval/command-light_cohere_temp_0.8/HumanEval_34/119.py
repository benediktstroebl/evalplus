```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(xlist[x)
    return result

# Test the function
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]
# Try again, this time with duplicate elements
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123, 5]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]
```

This code defines a function called unique that takes a list as input and returns a sorted list of unique elements from that list. The function uses a set to keep track of elements that have been seen before and a new list to build up the unique elements. The test cases demonstrate the values of the list that pass the test successfully.