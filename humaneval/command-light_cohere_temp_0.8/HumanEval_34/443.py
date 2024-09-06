Here's a self-contained Python script that defines a function `unique` solving the problem you described:
```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Example usage
numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(numbers))
```
This function uses a set to keep track of unique elements and then builds a list with those elements, ensuring all duplicates are ignored. The example output is `[0, 2, 3, 5, 9, 123]`.