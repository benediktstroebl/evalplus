Here's a Python script that solves the given problem with an efficient algorithm using a sorted list:
```python
def pluck(arr):
    # Sort the list and remove odd numbers
    even_indices = [i for i, n in enumerate(arr) if n % 2 == 0]
    if even_indices:
        return [min(arr[even_indices]), even_indices.index(min(arr[even_indices]))]
    else:
        return []
```

The `pluck` function takes an array (`arr`) as input and first filters out the even numbers from the array using a list comprehension. Then, it checks if the filtered list is not empty, and returns the plucked node, which is the first element of the even numbers list and its index using the `index` function. If the array has no even numbers, an empty list is returned. 

This approach takes advantage of Python's list comprehension and efficient filtering, ensuring the code is both effective and easy to understand.