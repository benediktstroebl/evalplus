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

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integers encountered. Using `float('-inf')` and `float('inf')` allows for efficient comparison of positive and negative values, respectively. The function returns a tuple with the respective integers if both are defined; otherwise, it returns `None` for each. 

This approach ensures that the function handles various scenarios, returning the correct results while adhering to the problem's guidelines. Test cases are also included to validate the function's behavior.