```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x +1))

# Test the function with a sample list
list_to_sort = [5, 6, 3, 4, 2]
result = sort_even(list_to_sort)
print(result)  # Expected output: [3, 6, 5, 4, 2]
```
This script defines a function `sort_even` that takes a list `l` as input and returns a sorted list `l'` such that the values at even indices are equal to the values of the corresponding even indices in the original list, while maintaining the original order of the odd indices. The sorted list is identical to the original list in the odd indices.