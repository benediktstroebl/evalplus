```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # initialize maximum element
    max_so_far = float('-inf')

    # traverse the list and update max_so_far if a number is greater than max_so_far
    for num in l:
        if num > max_so_far:
            max_so_far = num

    return max_so_far
```

This code block implements an algorithm that uses a variable called max_so_far to keep track of the maximum value encountered so far. The algorithm runs through a list of numbers, comparing each number to the current max_so_far value. If a number is bigger than max_so_far, the value of max_so_far is updated. Finally, the function returns the max_so_far value, which will be the largest number in the list. This approach ensures that the function can handle negative numbers as well as positive ones.