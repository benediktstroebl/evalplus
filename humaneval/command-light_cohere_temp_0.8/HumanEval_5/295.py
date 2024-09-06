Here is a self-contained Python function that solves the problem of inserting a specified delimiter between every two consecutive elements in a list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]) + delimeter
        else:
            result.append(numbers[i])
    return result
```
This function takes a list of integers numbers and a delimiter as input and returns a new list with the elements of the input list interspaced by the specified delimiter.