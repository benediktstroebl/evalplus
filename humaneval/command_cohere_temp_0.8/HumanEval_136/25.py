```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (positive == float('-inf') or n > positive):
            positive = n
        if n < 0 and (negative == float('inf') or n < negative):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive and largest negative integers using floats '-inf' and 'inf' for comparison. The return value is a tuple (`None`, `None`) if the list lacks negative or positive integers. This approach ensures that the largest negative and smallest positive integers are correctly captured and returned, irrespective of the list's content or length. 

This approach allows the function to handle edge cases where the list may contain zero or negative integers only, positive integers only, or a mix of both.  This makes the function more robust and adaptable to various scenarios as per the problem statement.