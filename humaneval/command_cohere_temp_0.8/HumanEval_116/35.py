```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function then sorts the array based on these values. After sorting, the function returns the sorted array.

This approach solves the problem by first sorting the array based on the number of ones in their binary representation and then, in case of a tie, sorting based on the decimal value of the numbers. 

This solution is concise and efficient, as it uses the built-in `sort` function with a custom key to handle the sorting logic. It avoids explicit looping and sorting algorithms, making it suitable for handling various input sizes.