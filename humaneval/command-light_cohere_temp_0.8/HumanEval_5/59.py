Here's a Python script that encapsulates the solution:
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
This function, `intersperse`, takes a list of integers `numbers` and a `delimiter` as input and returns a list where every other element is preceded by a `delimiter`.