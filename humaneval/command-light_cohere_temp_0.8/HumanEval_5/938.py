Here's a self-contained Python function that solves your problem of inserting a delimiter between every other element in a list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for num in numbers:
        result.append(num)
        if len(result) != 1 else result.append(delimiter)
    return result
```
This function takes a list of integers **numbers** and a delimiter integer **delimiter** as input, and returns a new list with the elements of the original list interspaced by the specified delimiter.