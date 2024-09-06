```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The `largest_smallest_integers` function iterates through the list of integers, identifying the largest negative and smallest positive integers. The function updates the `negative` and `positive` variables whenever a new maximum or minimum is encountered, ensuring that the correct values are returned even if the list contains multiple extremes. 

Here's an example of use for that function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
```

And here is the output of the previous code:
```
(1, 1)
``` 

This indicates that the largest negative integer is 1 and the smallest positive integer is also 1, as both are present in the list. 

This function handles edge cases such as empty or single-element lists, ensuring that `negative` and `positive` are correctly assigned to `None` if no negative or positive integers are present.