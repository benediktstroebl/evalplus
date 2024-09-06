Here's a self-contained Python function that implements your problem's solution:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        if i > 0: result.append(delimiter)
        result.append(n)
   
    return result
```
This function takes a list of integers and a delimiter as input, and returns a new list with the integers interspaced by the specified delimiter.