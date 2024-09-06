```python
def median(lst):
    # Sort the list
    lst.sort()
    
    # i in range(len(lst) // 2):
        # Find the index of the middle element
        mid = lst.indexof(lst[(i+1)::2])
        return (mid + (len(lst) - i - 1) * lst[mid]) / 2

# Example usage
lst = [1, 2, 3, 4, 5]
print(median(lst))  # Output: 2.0
```