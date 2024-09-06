```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            result.append(num + delimeter)
        else:
            result.append(num)
    return result
```
The code provides a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with numbers separated by the specified delimiter. The code works by iterating through the input list and appending the next number to the list after the number is an even index or appending the current number as the list element if the index is an odd index.