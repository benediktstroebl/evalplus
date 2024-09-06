```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple `(a, b)`, where `a` is the largest integer of those in the list that are less than zero and `b` is the smallest integer of those in the list that are greater than zero. If the list contains no negative or positive integers, both values should be returned as `None`.

The provided code solves the problem by using two nested list comprehensions. The first comprehension extracts all negative integers from the list using the condition `x < 0` and assigns the maximum of these to the variable `negative`. Meanwhile, the second comprehension extracts all positive integers from the list using the condition `x > 0` and assigns the minimum of these to the variable `positive`. 

Finally, the function returns a tuple containing `negative` and `positive`.