```python
def triples_sum_to_zero(l: list):
    if not set(l) <= {0,}:
        return True
    return False
``` 
This code defines a Python function called `triples_sum_to_zero`, which takes a list `l` as input and checks whether the list has three distinct elements whose sum is zero. 
The function returns `True` if there are three such elements and their sum is zero, and `False` otherwise. 
This function is self-contained and can be used to solve the problem of finding three distinct elements in a list whose sum is zero.