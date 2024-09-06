```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem by using a key function to create a sort key for each element in the array. The key is a tuple of two elements: the first element is the number of ones in the binary representation of the number, and the second element is the negative decimal value of the number. This ensures that the array is sorted first by the number of ones in the binary representation and then by decimal value in descending order.