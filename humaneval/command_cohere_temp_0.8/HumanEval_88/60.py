```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:len(array)//2+1:-1]
    else:
        return array[::-1]
```
This function relies on the parity of the length of the array to determine whether to sort in ascending or descending order. The `[len(array)//2+1:-1]` slicing is used to get the middle element and all elements after it in ascending order when the length of the array is odd, effectively sorting the array. When the length of the array is even, it's reversed in-place to sort the array in descending order. This achieves the desired sorting behavior based on the specified condition. 
The function also handles the edge case where the input array is empty, which is mentioned in the note of the problem statement, and doesn't modify the original array.