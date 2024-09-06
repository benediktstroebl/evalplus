```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [([1, 2, 3], 4), [10, 20, 30], [40, 60, 80])
test_results = [intersperse(test_data[0], test_data[1]), intersperse(test_data[1], test_data[2]), intersperse(test_data[2], test_data[3])]

print(test_results)
```