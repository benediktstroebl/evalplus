```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [4, 2, 3]
print(intersperse(numbers, 4))  # Expected output: [4, 8, 12, 16, 20]
```
This Python function, `intersperse`, takes a list of integers `numbers` and a delimiter `delimeter` as input. It then uses list comprehension to iterate over the elements of the input list, adding the current element and the result of multiplying the delimiter to the previous element. The result is a new list with the elements separated by the specified delimiter.