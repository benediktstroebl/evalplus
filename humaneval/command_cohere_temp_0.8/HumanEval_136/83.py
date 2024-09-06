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

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive and largest negative integers, updating the respective variables (`positive` and `negative`). The function returns a tuple containing these two values. If the list lacks either positive or negative integers, the corresponding value in the tuple is set to `None`. 

The script assumes a test suite is available to validate the code. Ensure you have it contained in the same directory as the script or adjust the file paths accordingly.