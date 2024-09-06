Here's the Python script with a self-contained function `remove_duplicates()` that solves the problem of removing duplicate integers from a list:

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This function, when given a list of integers, goes through each number and compares it with all previously seen numbers in the seen set. The function then adds the numbers that are not in the seen set and stores them in the result list.