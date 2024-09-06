```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n-1) // 2] + lst[n//2]) / 2
    else:
        return lst[(n-1) // 2]

# Test the function
for i in range(0, 10):
    assert median([i,i+1]) == i+1, "Should return the element directly"

for i in range(0, 10):
    assert median([-10,i,i+1]) == -10 + i, "Should return median of negative numbers"

for i in range(0, 10):
    assert median([i,i+1, -10]) == -10 + i, "Should handle mixed data"

for i in range(0, 10):
    assert median([-10, -10, -10, -10, -10, i, i+1]) == -10 + i, "Incorrect mixed data"
```