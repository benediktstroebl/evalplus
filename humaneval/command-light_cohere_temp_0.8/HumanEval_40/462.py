```python
def triples_sum_to_zero(lst):
    n = len(lst)
    for i in range(n // 3):
        sum_remaining = sum(lst[i+3:])
        if sum_remaining < 0:
            return False
    return True

# Test the function
for i in range(10):
    if not_zero = triples_sum_to_zero([i, i+2, i+3]) and not_zero:
        print(f"{i} failed.")
    else:
        print(f"{i} passed.")
```