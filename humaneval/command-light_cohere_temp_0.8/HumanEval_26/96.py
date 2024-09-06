Here's a self-contained Python function that removes duplicates from a list of integers:
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
This function utilizes a set to track unique integers and builds a new list with elements not previously encountered, effectively removing duplicates. 

The function is then tested with a sample input, demonstrating its functionality.