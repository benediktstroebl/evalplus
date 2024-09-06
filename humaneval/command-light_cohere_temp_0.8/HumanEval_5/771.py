```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1): 
        if i % 2 == 0:
            result.append(numbers[i]) + delimeter
        else:
            result.append(numbers[i])
    return result
  ```