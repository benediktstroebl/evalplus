```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test cases
test_get_positive = []
test_cases = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 2, 0, -6]]

for test in test_cases:
    result = get_positive(test)
    test_get_positive.append(result)

# Print results
for result in test_get_positive:
    print(result)
 ```