```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before sorting. Here, a lambda function `lambda x: (bin(x).count('1'), x)` is used. This function first converts the number `x` to its binary representation using `bin(x)`. It then counts the number of occurrences of '1' in this binary representation using `bin(x).count('1')`. This value is sorted in ascending order. For numbers with similar numbers of ones, their decimal value is used to sort them in ascending order.

The script passes the test cases specified in the problem and should work for other valid inputs.  Hava a look at the `lambda` function, it is a great way of passing an ad-hoc function without defining a named function. It is often used in situations like this where the function is only needed once (like in the `sort` function here) and does not need to be reusable. 

Let me know if you'd like me to explain anything in more detail!