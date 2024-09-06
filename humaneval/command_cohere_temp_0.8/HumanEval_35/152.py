```python
def max_element(l: list):
    """Return maximum element in the list.

    :param l: A list of numbers.
    :type l: list
    :return: The maximum element in the list.
    :rtype: int
    """
    # Initialize maxval to the first element in the list
    maxval = l[0]
    # Iterate over the list, and update maxval to the largest of maxval and the current element.
    for x in l:
        if x > maxval:
            maxval = x
    # Return the final maxval
    return maxval
```

This code defines a function called `max_element` that takes a list of numbers as input and returns the maximum element in the list. The function initializes `maxval` to the first element of the list, then iterates over the list, updating `maxval` to the largest of `maxval` and the current element. Finally, the function returns the final `maxval`. 

Here is an example of how to use this function:
```python
print(max_element([1, 2, 3]))  # Outputs: 3
```
```python
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Outputs: 123
```

The function can handle both positive and negative numbers and returns the correct maximum element for different input lists.