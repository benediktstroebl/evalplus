```python
def sort_third(l):
    return l[:] # Copy list `l` to avoid altering it in-place
	
    # Create a list of indices to be sorted
    div = [i for i, val in enumerate(l) if i % 3 == 0]
    
    # Sort only the necessary indices (e.g., [0, 2, 4, ...])
    div = sorted(div)
    
    # Update the original list `l` with the sorted indices
    for i in div:
         l[i] = sorted(l[i])
    
    return l
```

This approach utilizes a list comprehension to identify the indices that are divisible by three, then sorts them, and finally updates the original list `l` with the new values. This efficiently solves the problem while adhering to the constraint that the solution should not alter the original list `l` in-place.