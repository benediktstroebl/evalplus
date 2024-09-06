```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(xvoid)
    return result

# Test 1: Check unique elements from a list
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'b', 'c', 'd']
]

# Function call and check results
for test_case in test_cases:
    actual_result = unique(test_case)
    expected_result = [0, 2, 3, 5, 9, 123]
    assert actual_result == expected_result, f"Test {test_case} failed"
``` 
The code defines a function unique that takes a list lst as input and returns a list of unique elements in that list. It uses a unique elements technique to achieve this, which involves using a set to keep track of elements seen so far and only adding elements to the set that are not present. The code also has a test cases, and the unique function is called with each test case. The actual result is compared to the expected result, and the test passes if the two results are equal.