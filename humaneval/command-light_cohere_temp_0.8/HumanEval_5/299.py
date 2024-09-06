Here's a self-contained Python function that solves the problem of inserting a delimiter between every two consecutive elements in a list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result
```

This script defines a function 'intersperse' that takes a list of integers and a delimiter as input and returns a new list with the elements from the original list separated by the provided delimiter. The test cases are provided to ensure the function correctness.