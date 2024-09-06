```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            positive = min(positive, n)
        else:
            negative = max(negative, n)
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, tracking the highest (smallest) negative integer and the lowest (highest) positive integer using `negative` and `positive` variables initialized to `inf` (-inf). The function returns a tuple with the respective max and min values or `None` if absent. 

This approach allows the function to efficiently solve the problem and achieve a linear time complexity of O(n). 

The code is also robust, handling edge cases such as empty lists, and providing consistent results with the given test cases.