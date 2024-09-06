Here's a solution to the markdown code block problem using Python:

```python
def remove_duplicates(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This function, remove_duplicates, takes a list of integers as input and returns a new list with unique integers. It uses a set to keep track of duplicate numbers and creates a new list with any numbers that were not in the seen set. This process ensures that each number only appears once in the output.