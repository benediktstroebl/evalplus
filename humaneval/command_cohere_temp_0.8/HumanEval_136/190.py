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

The `largest_smallest_integers` function iterates through the list of integers, identifying the largest negative and smallest positive values. The function optimizes the search process by updating `negative` and `positive` only when a new maximum or minimum is encountered, improving efficiency for larger lists.

This approach ensures that the correct values are returned while handling various scenarios, including lists with no negative or positive integers. The function is designed to work seamlessly with the given problem description and provide clear and concise results.