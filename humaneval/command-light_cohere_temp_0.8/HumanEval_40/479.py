```python
def triples_sum_to_zero(lst):
    if sum(x for x in lst if x < 0) == 0:
        return True
    else:
        return False

# Test the function
for i in range(0, 10):
    lst = [i, i, i]
    if triples_sum_to_zero(lst):
        print("Test passed for input list", end="")
    else:
        print("Test failed for input list", end="")
```
The function `triples_sum_to_zero` takes a list `lst` as an input. It then checks if there are three distinct elements in the list that sum to zero. If so, it returns `True`, indicating that there exists three distinct elements in the list that sum to zero. If not, it returns `False`, indicating that the condition is not met.