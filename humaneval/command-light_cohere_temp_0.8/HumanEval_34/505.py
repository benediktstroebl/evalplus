```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# test the function  
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_unique))
```