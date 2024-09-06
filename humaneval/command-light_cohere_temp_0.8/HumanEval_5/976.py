```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
assert len(result) == 6
print(result)  # this will print [5, 8, 6, 4, 8, 3]
```