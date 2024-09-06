```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimeterer)
        result.append(num)

    return result
```

This script defines a function `intersperse` that takes in a list of integers `numbers` and a delimiter `delimiter` as input and returns a list with the integers interspaced by the provided delimiter. The code is self-contained and efficient, following the best practices of Python programming.