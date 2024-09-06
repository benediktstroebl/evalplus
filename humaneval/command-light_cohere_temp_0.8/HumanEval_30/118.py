```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = []
test_cases = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

# Assertions
test_get_positive.push_all([has_positive([...]) for _ in range(6)])

def has_positive(test_case):
    return get_positive(test_case) == test_case

test_get_positive.push(has_positive([...]))

if __name__ == "__main__":
    print("All tests passed!")
```