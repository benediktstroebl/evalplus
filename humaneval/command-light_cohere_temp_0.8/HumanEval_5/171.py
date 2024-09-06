Here is a Python script that contains a self-contained function that solves the problem of inserting a specified delimiter between every two consecutive elements in the given list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n+delimeter * n)
    result.append(n)
   return result
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input and returns a new list where every other consecutive pair of elements is separated by the `delimiter`.