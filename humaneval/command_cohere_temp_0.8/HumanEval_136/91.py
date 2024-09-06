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

The `largest_smallest_integers` function works by setting initial values for `positive` and `negative` to represent the smallest and largest values that they have seen so far. Then, it iterates over the list, updating these values as needed using conditions related to edge cases where the initial values are set to `float('-inf')` and `float('inf')`. Finally, the function returns a tuple containing the largest negative integer and the smallest positive integer from the list, or `None` if none are present. 

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0])) 
```

This will output:
```bash
(None, 1)
(None, None)
(None, None)
```

This is consistent with the examples provided in the prompt.