```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case 1
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 8, 3]

# Test case 2
numbers = [1, 2, 3]
delimiters = [4, 8, 2]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 8, 4, 2, 8, 3]

# Test case 3
numbers = [1, 2, 3]
delimiters = [4, 2, 6]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 8, 2, 6, 3]
```
The function `intersperse` uses the `enumer` function to iterate through the list, adding the `delimiter` value between every other element.  It also uses a list comprehension to return the final list with all the values with appropriate separators.