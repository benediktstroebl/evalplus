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
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(input_list))
```