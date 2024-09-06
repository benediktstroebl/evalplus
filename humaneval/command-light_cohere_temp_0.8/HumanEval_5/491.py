```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimeter)
        result.append(num)
    result.append(delimiter)
    return result
```
The function `intersperse()` takes a list of integers `numbers` and a delimiter `delimiter` as input. It then iterates through the numbers and appends them to the result list, followed by the delimiter. Finally, it returns the list of integers.