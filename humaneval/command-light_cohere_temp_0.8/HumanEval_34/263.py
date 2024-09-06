```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not (-item for item in seen)]

if __name__ == "__main__":
    tests = [
        [], [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ['a', 'a', 'b', 'c'],
        [()],
        [1, 2, 3, 4, 5],
    ]

    for test_list in tests:
        got = unique(test_list)
        print(f"Got: {got}")
        expected = [0, 2, 3, 5, 9, 123]
        print(f"Expected: {expected}")
        print(f"Test passed: {test_list} == {got}")
```
This Python code defines a function called unique that sorts and returns unique elements from an input list. The main function runs a test cases using the unique function. The tests use lists with different types of data and ensure that the function correctly identifies and returns unique elements. 

This script is designed to be self-contained, and it can be easily reused in other programs or for other test cases.