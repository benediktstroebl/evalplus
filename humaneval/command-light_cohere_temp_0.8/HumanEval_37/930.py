```python
def sort_even(lst):
    return lst[:][::2] + lst[1:][::-1]

#Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [0, 10, 1, 9],
    [7, 8, 9, 10],
]

# Function call and testing
for test_case in test_cases:
    actual = sort_even(test_case)
    assert actual == [3, 6, 5, 4], f"Test {test_case} failed."
```