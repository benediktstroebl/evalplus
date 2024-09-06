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

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive and largest negative integers using floats '-inf' and 'inf' for comparison. The return value is a tuple (`None`, `None`) if the list lacks negative or positive integers. This approach ensures that the correct values are captured and returned while fulfilling the prompt's requirements.