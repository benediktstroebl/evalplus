```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, None]]

# Test cases
test_unique = [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123],),
    ([],),
    ([123, 45, 123],),
    ([1, 2, 3, 4],),
    ([-10, -20, -100],),
    ([1, 2, 3], [1, 2])
]

for test_case in test_unique:
    assert unique(test_case) == get_unique_elements(test_case)

def get_unique_elements(test_case):
    seen = set()
    return [x for x in test_case if not in seen and x not in [-None, None]]
```
This solution defines a unique function that takes a list as input and returns a list of unique elements in the list. The function uses a unique() function to filter out duplicates and return only unique elements in a sorted order.

The code also includes test cases to verify the correctness of the unique() function with various input lists. 

You can use this solution to solve the problem of finding unique elements in a list in a single, self-contained manner.