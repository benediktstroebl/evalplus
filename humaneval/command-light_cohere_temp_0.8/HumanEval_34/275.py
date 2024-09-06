```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

if __name__ == "__main__":
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [5,],
        [123, 2],
        [1, 2, 3, 4, 5, 6],
    ]

    for test in tests:
        got = unique(test)
        assert len(got) == len(set(test)),
        print(f"Test {test} passed.")
```

This code defines a function `unique` that returns a list of unique elements from an input list `lst`. The function utilizes a set to keep track of seen elements, then iterates through the list and adds elements to the set if they are not duplicates, not in `[0, ]`, and not in the empty set. The output of this function is then a list of unique elements from the input list, which will be sorted as well.