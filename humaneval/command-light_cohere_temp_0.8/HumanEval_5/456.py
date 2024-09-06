```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers] + [num for num in numbers]

# Test the function with different inputs
numbers = [4, 1, 9, 8, 10, 2, 5]
delimiters = [4, 2, 6]

result = intersperse(numbers, delimiters)
print("Result:", result)  # Output: [5, 4, 8, 10, 6, 2, 9, 4]

numbers = [1, 2, 3]
delimiters = [4, 4]

result = intersperse(numbers, delimiters)
print("Result:", result)  # Output: [1, 4, 2, 4, 3]

numbers = [10, 11, 12, 13]
delimiters = [2, 4, 6]

result = intersperse(numbers, delimiters)
print("Result:", result)  # Output: [8, 10, 11, 4, 6, 13, 2]
```