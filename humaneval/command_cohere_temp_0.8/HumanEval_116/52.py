```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in the binary representation of a given number. It utilises `bin` to convert decimal numbers to binary, and `count` to find the count of occurrences of `1` in the binary representation. 

The `sort_array` function then utilises a lambda function to sort the array, first by counting the ones in the binary representation using the `count_ones` function, and then by the decimal value in descending order in case of a tie. 

This solution is concise and efficient in line with Python conventions, and will sort the arrays according to the specified criteria, fulfilling the given task for the provided `sort_array` function.