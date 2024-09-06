```python
def triples_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l) and all(x != 0 for x in l)
``` 
You can use this function with a test list, and it will return True or False accordingly.