```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test cases
test_get_positive = [
    []
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

# Function call and testing
for case in test_get_positive:
    actual_result = get_positive(case)
    print(f"Case {case}: Expected [positive numbers] -> {actual_result}")
```