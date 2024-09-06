Here's the provided self-contained Python function that inserts a number 'delimiter' between every two consecutive elements of an input list:

```python
def decorate(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
        result.append(num)
    return result
```

This function will take an input list of integers and a single integer 'delimiter', and will return a list with the original numbers separated by the 'delimiter'.