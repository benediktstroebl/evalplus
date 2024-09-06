```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:len(array) // 2] + array[len(array) // 2:][::-1]
    else:
        return array[len(array) // 2:][::-1] + array[:len(array) // 2]
```

The function takes an array of integers as input and checks whether the length of the array is odd or even to sort the array accordingly. If the length of the array is odd, the middle element is used as the pivot, and the sorting is performed on either side of the pivot in ascending order, leaving the pivot in its original place. If the length of the array is even, the two middle elements are used as the pivot, and the sorting is performed above and below the pivot in descending order, leaving the pivot in its original place. Ultimately, the sorted array is returned.