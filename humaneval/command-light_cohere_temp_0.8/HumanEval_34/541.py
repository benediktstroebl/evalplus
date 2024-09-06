```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ""]]

# Test 1: [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_cases = [list(range(1,10)), [5,3,0,123,2], [5,3,9,1,4,23]]
for test_list in test_cases:
    assert unique(test_list) == [0, 2, 3, 5, 9, 123]
```
This Python code defines a function called unique that returns a list of unique elements from a given input list. It uses a fact-style inference to filter out duplicate elements, and the test cases are created to ensure that the unique() function produces the correct output.