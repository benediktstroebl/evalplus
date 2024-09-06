```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
    result.append(num)
    result.append(delimiter)
    return result
```

This code defines a function `intersperse` that takes in two parameters: a list of integers `numbers` and an integer `delimeter`. It then inserts the `delimeter` between every two consecutive elements of the `numbers` list, and finally returns a new list with the elements in it order.