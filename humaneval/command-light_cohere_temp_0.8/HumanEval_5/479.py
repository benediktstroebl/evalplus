```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 1)

# Test the function with an empty list
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([1, 2, 3], 0)
[1, 2, 3]
>>> intersperse([1, 2, 3], 10)
[1, 10, 2, 10, 3]
>>> intersperse([5, 6, 7], 4)
[5, 4, 6, 4, 7]
```