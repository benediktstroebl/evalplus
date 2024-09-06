```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test cases
tests = [
    [list(["abc", "def", "abc", "cdef"], return_value=["abc", "def"])
    [list(["a", "bc", "c"], return_value=["a", "bc"])
    [list("Hello", "olleh", "ello"), return_value=["Hello", "olleh", "ello"]
    [1, float("inf"), 3], return_value=[1, float('inf'), 3]
    [0, 2, float("inf"), float("inf")], return_value=[0, 2, float('inf')]
]

for test_case in tests:
    actual_result = unique(test_case[0])
    expected_result = test_case[1]
    print(f"Test case {test_case}: actual ({actual_result}), expected ({expected_result})")
    assert actual_result == expected_result, f"Test case {test_case} failed"
```  This code defines a function unique that returns a list of unique elements from the input list lst. It uses the unique elements in Python, which allows you to perform set-like operations on iterables. The code also includes test cases that cover different scenarios, and it uses the assert statement to verify if the actual result matches the expected result for each test case.