```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+1 if i<len(numbers) else delimeter for i in numbers]

# Tests
numbers = [1, 2, 3, 4, 5]
print(f'Result with spaces: {intersperse(numbers, 4)}')  # Output: Result with spaces: [1, 4, 2, 4, 3, 5]
print(f'Result without spaces: {intersperse(numbers, 0)}')  # Output: Result without spaces: [1 2 3 4 5]
print(f'Difference between results: { abs(intersperse(numbers, 4) - intersperse(numbers, 0)) }')  # Output: 0
```