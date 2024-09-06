```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The `largest_smallest_integers` function iterates through the list of integers and identifies the largest negative integer and the smallest positive integer. The function compares these values and returns them, or `None` if no negative or positive integer is found, aligning with the problem's expectations.

This approach allows for efficient identification of the largest negative and smallest positive integers in the list while maintaining a concise and readable code structure.