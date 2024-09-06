```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:len(array) // 2] + array[len(array) // 2:][::-1]
    else:
        return array[len(array) // 2:][::-1] + array[:len(array) // 2]
```

The function takes an array of integers as input and checks whether the length of the array is odd or even to sort the array accordingly. If the length is odd, it sorts the array from the middle to the end in reverse order and leaves the beginning as it is. If the length is even, it sorts the array from the beginning to the middle in reverse order and leaves the end as it is.