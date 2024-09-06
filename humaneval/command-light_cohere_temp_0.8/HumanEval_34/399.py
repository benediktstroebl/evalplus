```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, []]]

# Test cases
tests = [
    dict(zip(['asdf'], [
        unique([5, 3, 5, 2, 3, 3, 9, 0, 123]),
        unique([])     ,
        unique([1, 2, 3, 4, 5]) ,
        unique([0, 1, 2, 3])
    ])
]

# Run the tests
for test in tests:
    assert unique(*test) == test[1]
```
The code provides a function called `unique` that returns a list containing unique elements from the input list `lst`. It uses a set called `seen` to keep track of the elements encountered. The function iterates through each element to the set to see if it's already present and then returns it if it's not. The test cases are provided to check the correctness of the `unique` function.