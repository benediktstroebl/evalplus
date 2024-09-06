```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:len(array)//2+1:-1]
    else:
        return array[::-1]
```
This function relies on the parity of the length of the array to determine whether to sort in ascending or descending order. The lambda expression array[:len(array)//2+1:-1] creates a slice that sorts the array in ascending order. On the other hand, the slice array[::-1] sorts the array in descending order.