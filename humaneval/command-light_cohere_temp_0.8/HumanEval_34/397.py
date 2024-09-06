```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

if __name__ == "__main__":
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [5, ],
        [3, ],
        [9, ]
    ]

    for test in tests:
        actual = unique(test)
        assert set(actual) == set(test), "Test failed: " + str(test) + " != " + str(actual)
```
This function `unique` returns a list with unique elements from the input list. The `tests` is used to check if the actual result matches the expected result. 

Please note that the provided test cases are not valid Markdown.  If's probably expecting code blocks to contain code, not just text.