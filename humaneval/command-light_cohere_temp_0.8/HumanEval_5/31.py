```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [4, 1, 2, 3]
test_delimiter = 4
test_results = intersperse(test_data, test_delimiter)

print("Test Results:", test_results)

numbers = [1, 2, 3, 4, 5]
delimiter = 4
new_list = intersperse(numbers, delimiter)
print("New List:", new_list)
```