Here is a self-contained Python function that solves the problem of inserting a number 'delimiter' between every two consecutive elements of an input list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [x, delimeter, x + delimeter, ... for x in numbers]
```

This function works by using a generator expression to create a new list with the elements of the input list separated by the specified 'delimiter'.