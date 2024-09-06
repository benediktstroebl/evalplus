```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
   return result
```
This function, `intersperse`, is designed to work with lists of integers and creates a new list with a specific delimiter between every other consecutive element in the original list. It effectively inserts the