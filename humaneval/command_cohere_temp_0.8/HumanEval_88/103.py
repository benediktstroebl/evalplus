```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script defines a function `sort_array` that sorts an array of non-negative integers. The sorting order is determined by the parity of the sum of the first and last elements: if the sum is odd, it sorts in ascending order, and if it's even, it sorts in descending order. The function uses the `sorted` function and customizes the sorting order with the `reverse` parameter. Importantly, the function returns a new array rather than modifying the original, adhering to the requirement specified in the problem statement.