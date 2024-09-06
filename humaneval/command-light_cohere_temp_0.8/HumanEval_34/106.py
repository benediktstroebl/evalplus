```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
return result
# Create list with duplicate values
my_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]

# Call the function and print results
print(unique(my_list))
```