Here's a Python script that solves the given problem with an efficient approach using generators, without the need for lists, and with a small memory footprint:
```python
def pluck(arr):
    evens = (x for x in arr if x % 2 == 0)
    return next((x, i) for i, x in enumerate(evens, 1) if x == min(evens), [])
```

The script employs Python's generator expression (`(x for x in arr if x % 2 == 0)`), to filter even numbers from the array. It then uses a generator expression with the `enumerate` function to find the index and value of the smallest even number. The `next` function is used to return the first item that satisfies the condition, or an empty list `[]` if no even numbers are found.

This approach drastically reduces memory consumption, especially for large input arrays, and provides a more efficient solution compared to creating a list for even numbers and then filtering and sorting them.