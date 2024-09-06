```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array. The `sort_array` function then uses a lambda to sort the array according to the number of ones in the binary representation in ascending order while retaining the original position of the ones. 

If there is a tie in the number of ones, the decimal value is used to break the tie and ensure numbers with fewer ones come first. The function returns the sorted array as described in the problem statement. 

This approach ensures that the array is sorted according to the specified criteria while being efficient and straightforward.