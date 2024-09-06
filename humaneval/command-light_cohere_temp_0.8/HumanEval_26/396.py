Here's the self-contained Python function to remove duplicates from an input list of integers:
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

The function uses a `set` to keep track of seen integers, then iterates through the input list. It adds each integer to the set if it hasn't been seen before, then adds it to the results list. 

This function is self-contained and does not require any external variables or functions to solve the problem.