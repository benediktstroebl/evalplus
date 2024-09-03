```python
def smallest_change(arr):
    arr = list(set(arr))        # Remove duplicates
    return sum(1 for i in range(len(arr)) for j in range(len(arr)-1-i) if arr[i] != arr[j])
```
The function works by first removing any duplicates from the array, then iterating from the beginning of the array and comparing each number to the subsequent ones, counting the differences. The lowest number of differences is the minimum number of changes required to make the array palindromic.