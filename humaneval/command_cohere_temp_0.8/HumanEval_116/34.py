```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in a given number's binary representation. It also defines the `sort_array` function, which sorts the given array using a custom sorting key. This key is a tuple, with the first element being the result of `count_ones(n)`, and the second element is `-n` which ensures that in case of a tie, the numbers with more zeros in the front will come first. The resulting sorted array is returned. The code is written to meet the specified requirements and expected outputs.