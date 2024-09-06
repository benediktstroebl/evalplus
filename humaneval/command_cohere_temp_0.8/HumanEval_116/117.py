```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` function calculates the number of ones in the binary representation of a given number. The `sort_array` function sorts the array using the `count_ones` function as the key to sort them firstly according to the number of ones in the binary representation and, in case of a tie, sorts them by their decimal value in descending order.