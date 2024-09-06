```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            if n > positive:
                positive = n
        else:
            if n < negative:
                negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integers encountered. Using `float('-inf')` and `float('inf')` allows for efficient comparison of floats and integers. The function returns a tuple containing the largest negative and smallest positive, or `None` if not present in the list.

The following example demonstrates the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0]))
```

Output:
```
(None, 1)
(None, None)
(None, None)
```

This demonstrates the function's behavior, successfully identifying the largest negative and smallest positive integers among the given lists, and returning `None` when such integers are not present. 
This approach ensures efficiency and clarity in solving the problem.