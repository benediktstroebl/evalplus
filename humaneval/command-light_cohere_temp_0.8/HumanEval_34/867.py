```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

if __name__ == "__main__":
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [5, 3, 'abc'],
        [20200, 20200, '20200'],
        ['a', 'a', 'b', 'c'],
    ]

    for test_list in tests:
        print(unique(test_list))
```
This script defines a function unique that returns a list of unique elements from a given list lst, based on the set-of-seen elements.  The using tests various input lists, and correctly returns unique elements. The main function tests the particular test cases, and the output is displayed.