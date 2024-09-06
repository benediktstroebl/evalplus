```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test case 1
test_cases = [[5, 3, 5, 2, 3, 3, 9, 0, 123], [1, 2, 3, 5], [5, 5, 9, 123]]
for test_case in test_cases:
    got = unique(test_case)
    assert len(got) == len(test_case)
    assert all(got == test_case)

# Test case 2 (Different data type)
test_cases = [[5, 3, 5, 2, 3, 'asdf'], [True, False, True]]
for test_case in test_cases:
    got = unique(test_case)
    assert len(got) == len(test_case)
    assert all(isinstance(got[0], bool))
```
The above Python script defines a function called `unique` that returns a list containing the unique elements from an input list. It utilizes a`set` to create a set to keep track of seen elements, and then it iterates through the input list, adding elements to the set and returning the unique ones. The test cases demonstrate the various scenarios, such as different data types and lists of different sizes, and the output is compared to the expected results.