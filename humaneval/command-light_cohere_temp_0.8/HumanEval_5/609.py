```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

numbers = [1, 2, 3]
delimiters = [4, 4, 8]
result = intersperse(numbers, delimiters)
print(result)
```