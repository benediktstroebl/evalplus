Here's the Python code with a self-contained function that solves the problem:
```python
def triples_sum_to_zero(lst):
    if not in lst or len(lst) < 3:
        return False
    s = sum(lst)
    return (s <= 0) and triples_sum_to_zero(lst[:2])
```
Do you have any questions about the code?