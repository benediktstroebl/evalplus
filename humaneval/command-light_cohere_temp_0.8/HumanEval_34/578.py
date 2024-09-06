```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Tests
test_passes = [unique([5, 3, 5, 2, 3, 3, 9, 0, 123]),
            unique([1, 2, 3, 4, 5, 6]),
            unique([True, False, True])]

for func, expected in test_passes:
    assert func == expected, "Function {} failed tests!".format(func)
```
This code defines a function `unique` that returns a list with unique elements from the input list `lst`. It uses a set `seen` to keep track of the items encountered, and when an element is encountered for the first time, it's added to the set and also added to the result list.  The code includes tests to verify the correctness of the `unique` function with a variety of input lists.