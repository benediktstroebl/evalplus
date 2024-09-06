```python
def triples_sum_to_zero(l):
    return sum(x == y for x, y in zip(l, l[1:])) == 0

# Test the function
for i in range(10):
    if triples_sum_to_zero([i, i+2, i+4]) == True:
        print(f"test passed, i={i}")
```