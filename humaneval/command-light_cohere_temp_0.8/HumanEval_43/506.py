```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    return False

# Test the function with various lists of integers
for i in range(0, 10):
    print(f"{i+1}: { pairs_sum_to_zero([i, i+1])}")
```