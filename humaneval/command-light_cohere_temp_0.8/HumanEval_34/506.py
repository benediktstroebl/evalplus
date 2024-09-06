```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

# Test cases
tests = {
    "Input: [5, 3, 5, 2, 3, 3, 9, 0, 123]"
    .that: [0, 2, 3, 5, 9, 123]
    "Input: []"
    .that: []
    "Input: [5, 3]"
    .that: [3]
    "Input: [9]
    .that: []
    "Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]"
    .that: [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

for test_case, expected in tests.
 unique(test_case):
    actual = unique(test_case)
    print(f"Test case [{test_case}] => {actual} -> {actual}")
    print()
``` 
This script defines a function called unique, which takes a list as input and returns a new list with unique elements from the original list. The function utilizes the unique elements and a set to keep track of the elements that have already been seen, then it filters out any repeated elements from the original list.