```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test the function with various inputs
tests = [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123],),
    ([1, 2, 3, 4, 100],),
    ([],),
    ([1, 2, 3, 'a'],)
]

for test, expected in zip(tests, unique(test)):
    print(f"Test: {test} -> {expected}")
``` 
This script defines a function called unique that takes a list lst as input and returns a new list with the unique elements from the original list. It uses a toolset to keep track of the elements that have already been seen, and then it iterates through the original list and adds each element to the set if it is not in the set and is not None. The output is the expected list of unique elements.