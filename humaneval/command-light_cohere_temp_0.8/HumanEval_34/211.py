```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not bool(0)]

if __name__ == "__main__":
    tests = [
        [],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ['a', 'a', 'b', 'c'],
        [2, 2, 4, 5, 'abc'],
    ]

    for test_list in tests:
        print("Test:", test_list)
        unique_result = unique(test_list)
        print(unique_result)
```
This script defines a function named unique that takes a list as input and returns a new list containing only the unique elements. It uses a particular set to keep track of the seen elements, and then iterates through the original list, only adding elements that are not in the set and not bool(0) (which represents the empty set). The function is tested against multiple input lists and the results are printed to the console.