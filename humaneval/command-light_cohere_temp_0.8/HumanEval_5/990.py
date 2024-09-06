```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list"""
    res = []
    for num in numbers:
        res.append(num)
        res.append(delimeter)
    return res
```
The provided code defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input and returns a new list where the `delimiter` is inserted between every two consecutive elements. 
This is a self-contained way to solve the problem and pass the tests.