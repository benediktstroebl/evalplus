```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before comparison. Here, it uses the `bin` function to get the binary representation of each element and the `count` method to count the number of ones in each binary representation. Elements with more significant "1" values sort first, and if there is a tie, it sorts based on the decimal value of the elements.