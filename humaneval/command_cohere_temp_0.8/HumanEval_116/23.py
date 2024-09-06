```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before sorting. Here, a lambda function `lambda x: (-bin(x).count('1'), x)` is used. For each number `x` in the list, `bin(x)` returns a string representing its binary representation. `count('1')` counts the number of '1's in this binary representation. This count is negated (made negative) because we want to sort these numbers in ascending order. Finally, the original number `x` is also part of the key to break ties if two numbers have the same number of '1's in their binary representation.

The script sorts the array according to the specified criteria, ensuring that numbers with more binary '1's are sorted first, and if two numbers have the same number of '1's, their decimal value determines their order.