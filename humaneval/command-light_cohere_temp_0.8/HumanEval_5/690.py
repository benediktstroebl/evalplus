```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result
```
The function `intersperse()` adds a separator number to every other element in the input list, except for even indexes. The input list and separator number are the parameters of the function.