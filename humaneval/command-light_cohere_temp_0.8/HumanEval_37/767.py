```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)

# Test cases
test_suite = [
    ( [1, 2, 3],),
    ( [5, 6, 3, 4],),
    ( [100, 200, 150],),
]

for test in test_suite:
    actual = sort_even(test)
    expected = [3, 6, 5, 4]  # [0-based index]
    assert actual == expected
``` 
This function, sort_even, takes a list and returns a sorted list of the same elements but with values modified at the even indices to be equal to their original values plus 1. The test suite contains several test cases to verify the correctness of the function, and it uses the assert statement to check if the actual output matches the expected output for each test case.