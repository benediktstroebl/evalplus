```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (n < positive or positive == float('-inf')):
            positive = n
        if n < 0 and (n > negative or negative == float('inf')):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The function `largest_smallest_integers` works by setting `positive` and `negative` to appropriate initial values (-inf and inf respectively) to efficiently track the largest positive and smallest negative values. Then, it iterates through the list, updating the values as necessary. Ultimately, it returns a tuple containing the largest negative and smallest positive values. If the list contains no negatives or positives, respectively, None is returned instead. 

This approach ensures that the function efficiently solves the problem in a single pass, avoiding the need for additional iterations.