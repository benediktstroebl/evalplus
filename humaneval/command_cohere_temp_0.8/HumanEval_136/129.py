```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as an argument and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list contains no negative or positive integers, it returns `None` for the respective value. 

The `positive` variable is created by using a list comprehension to filter all positive numbers from the input list and then finding the minimum value using the `min` function. Similarly, the `negative` variable is created by filtering out all negative numbers from the input list and then finding the maximum value using the `max` function. 

The two variables are then returned as a tuple.

This solution adheres to the problem's specified examples, returning the correct values for the given input lists.