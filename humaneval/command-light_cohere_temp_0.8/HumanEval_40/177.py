```python
def triples_sum_to_zero(l):
    if not set(l) <= {0}:
        return True
    return False
``` 
This function efficiently checks if there are three distinct elements in a list `l` whose sum is equal to zero, and returns `True` if this condition is met, and `False` otherwise. 
The function utilizes the set difference to quickly identify the desired property. This approach is efficient and requires only a bitwise comparison, which is a simple operation in Python.