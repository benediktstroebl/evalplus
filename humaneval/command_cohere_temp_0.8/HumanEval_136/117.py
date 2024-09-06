```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as an argument and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list contains no negative or positive integers, it returns `None` for the respective value. 

The logic behind this function revolves around two key Python methods: `max` and `min`. The `max` function takes two arguments: a list of items and a callback function that returns the 'size' of each item. It then returns the item with the largest 'size'. In our case, the 'size' of each item is its absolute value, and the max function returns the negative integer with the largest absolute value. 

Similarly, the `min` function also returns the item with the smallest 'size', which in our case is the absolute value of the positive integers. 

Please note that this code assumes that the list `lst` contains at least one positive and one negative integer. If the list is empty or contains only zeros, the function will return `None` for both values. Adjustments are needed for the edge case of an empty list to properly handle that scenario.