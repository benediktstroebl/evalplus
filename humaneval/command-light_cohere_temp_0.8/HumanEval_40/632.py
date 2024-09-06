```python
def triples_sum_to_zero(lst):
    sum = 0
    for x in lst:
        if sum + x <= 0:
            return True
        sum += x
    return False

# Test the function
for i in range(0, 10):
    if triples_sum_to_zero([i, i, i]) == True:
        print(f"The list {i} passes the test.")
```