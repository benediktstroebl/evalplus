```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n)
        if i % 2 == 0:
            result.append(delimeter)
    return result
```

This script provides a function `intersperse` that takes a list of integers `numbers` and a delimiter `delimeter` as input, and it returns a list of integers with the delimiter inserted between every two consecutive elements. 

The function uses a loop to iterate over the input list of numbers, and it checks whether the index of the current element is an even number (i.ve inserting the number to the result list if the index is even).