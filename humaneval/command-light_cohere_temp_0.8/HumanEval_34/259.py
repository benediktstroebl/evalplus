```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float]

# Test case 1: Output should be [0, 2, 3, 5, 9, 123]
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2: Output should be [] (No duplicates should be present)
assert unique([1, 2, 3, 3, 4]) == []

# Test case 3: Output should raise TypeError
try:
    unique([(1), 2])
except TypeError as e:
    assert str(e) == "TypeError: Can only extract unique elements from sequence of mutable objects"
``` 
This code defines a function called `unique`, which takes a list as input and returns a new list containing only the unique elements from the input list. The function uses a set to keep track of the elements that have already been seen, and then it iterates through the input list, checking each element against the set to see if it is unique. The `assert` statements are then used to verify that the `unique` function is working correctly for various test cases.