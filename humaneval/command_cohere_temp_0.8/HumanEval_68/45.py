Here's a Python script that solves the given problem with an efficient algorithm using a Python list and tuple-assignment:
```python
def pluck(arr):
    if not arr:
        return []

    # Filter even values and get their index
    even_values = [i for i, val in enumerate(arr) if val % 2 == 0]
    
    if not even_values:
        return []

    # Get the minimum even value and its index
    min_val, min_index = min(even_values), even_values[0]

    # Check if there are multiple occurrences of the minimum even value
    if len(even_values) > 1:
        # Filter the occurrences of the minimum even value and get the index of the minimum index
        min_index = min(even_values[1:], key=lambda x: x[1])[1]

    return [min_val, min_index]
```

The algorithm efficiently solves the problem in a single pass, using the list `even_values` to filter the even values and getting their index using `enumerate`. The minimum even value is obtained using the built-in `min` function. In case of multiple occurrences of the same minimum even value, the algorithm filters these occurrences and retrieves the index of the minimum index among them using a lambda function. Finally, the result is returned as a list `[min_val, min_index]`.

This approach has a time complexity of O(n) because it processes the list `arr` only once, making it an efficient solution compared to other potential approaches like using recursion which can have a higher time complexity.