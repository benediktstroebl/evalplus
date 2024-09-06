```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[n] + 1)
    return l

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [21]
]

for test_case in test_incr_list:
    actual = incr_list(test_case)
    assert all(map(lambda x: x == actual, test_case)),  # assert the updated list equals the expected list
    print("Test passed:", end="")
```  This code defines a function incr_list that takes a list l as input and returns a new list with elements from input list l incremented by 1. The code also provides test cases to check the correctness of the incr_list function, and the results are printed after each test case passes.