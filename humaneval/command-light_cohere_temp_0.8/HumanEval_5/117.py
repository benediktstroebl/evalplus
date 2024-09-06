```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with different inputs
numbers = [4, 2, 1]
delimiters = [4, 2, 1]
result = intersperse(numbers, delimiters)
print(result)  # Expected Output: [5, 6, 3, 8, 5]

numbers = [1, 2, 3]
delimiters = [4, 4, 4]
result = intersperse(numbers, delimiters)
print(result)  # Expected Output: [1, 4, 8, 12, 16]

# Invalid Input Test
numbers = [1, 2, 3]
delimiters = [4, 5]
result = intersperse(numbers, delimiters)
print(result)  # Expected Output: Traceback (order may vary)
```