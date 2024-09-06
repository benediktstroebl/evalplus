```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x < 0]) <= 0:
        return True
    return False

# Test the function
for i in range(0, 10):
    if triples_sum_to_zero([i, i, i])):
        print("Yes")
    else:
        print("No")
```
The provided code defines a Python function `triples_sum_to_zero` that checks if a list of integers has three distinct elements whose sum is zero. The function returns `True` if it finds such, indicating that the list satisfies the given property. The tests at the
end, the code will print "Yes" if the property is satisfied and "No" if it is not satisfied, respectively.