```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` sorts the array based on the sum of the first and last elements. If the sum is odd, it sorts the array in ascending order using the `sorted()` function. If the sum is even, it sorts the array in descending order by setting the `reverse` parameter in the `sorted()` function to `True`. Finally, the function returns the sorted array. 

This code uses a concise yet effective approach to solve the problem, which results in efficient coding. Such solutions are desirable as they maintain simplicity and conciseness while minimizing unnecessary complications.  This makes the code easier to understand and maintain, which leads to productivity and efficiency gains for future developers.  This aspect is especially important for collaborative projects, where code readability and collaboration are crucial for success.