```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
return result
# Example usage:
# Input list
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
# Call the unique function
result = unique(input_list)
# Print the result
print("Result:", result)
```