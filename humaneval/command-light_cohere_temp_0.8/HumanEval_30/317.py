```python
def get_positive(input_list):
    positive = [num for num in input_list if num > 0]
    return positive

# Test cases
test_get_positive = []
test_cases = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for case in test_cases:
    test_get_positive.insert(case)
    assert len(get_positive(case)) == 4, f"Wrong length for positive numbers.
    assert all(num > 0 for num in get_positive(case)),
    assert get_positive(case) == [2, 5, 6, 3], f"Wrong output: {get_positive(case)}"
```
The above Python code defines a function `get_positive` that filters out negative numbers from an input list and returns a new list containing only the positive numbers. It provides test cases to test the function, ensuring that it returns the correct output for each case and adheres to the condition of having exactly four positive numbers.