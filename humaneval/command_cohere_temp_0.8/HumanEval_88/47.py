```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```

The `sort_array` function uses the sum of the first and last elements of the array to determine whether to sort in ascending or descending order. The sum is considered odd if it cannot be evenly divided by 2, which is determined by using the modulo operator (`%`). If the sum is odd, the list is sorted in ascending order. If the sum is even, the list is sorted in descending order. The `sorted` function is utilized to sort the array based on the provided logic. The parameter `reverse` ensures that the order is reversed if the sum of the first and last elements is even.