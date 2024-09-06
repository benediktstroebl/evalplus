```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

if __name__ == "__main__":
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [unique([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])],
        [['a', 'b', 'c'],
        [set('abc')],
    ]

    for test in tests:
        print(f"Test {test}")
        assert unique(test) == [0, 2, 3, 5, 9, 123], "Assert failed"
```
This code defines a function `unique` that returns a list with unique elements from the input list `lst`. The `seen` set is used to keep track of elements encountered. The `assert` statement is used to validate the output against the expected result.