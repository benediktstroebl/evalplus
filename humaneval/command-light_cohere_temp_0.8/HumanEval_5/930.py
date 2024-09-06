```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)]

#Test case 1
numbers = [1, 2, 3]
delimiters = [4, 4, 4]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 4, 3]

#Test case 2
numbers = [1, 2, 3]
delimiters = [4]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 4, 3]

#Test case 3
numbers = [1, 2, 3, 4, 5]
delimiters = [4, 4]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 4, 3, 4, 5]
```