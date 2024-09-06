```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

if __name__ == "__main__":
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [4, 6, 7, 8, 9],
        [ True, False, True],
        ['a', 'b', 'c'],
        [['a', 'b'], ['c']]
    ]

    for test in tests:
        print(unique(test))
```