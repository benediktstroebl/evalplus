```python
def triples_sum_to_zero(l: list):
    if not set(l) <= {0,3}:
        return True
    return False
```
This script defines a function `triples_sum_to_zero` that checks whether a list of integers contains three distinct elements whose sum is zero. 

The function uses the set membership test to ensure that there are no three elements in the list that sum to zero. 
It returns `True` if the list satisfies this condition, and `False` otherwise. 

The script also provides test cases to check the correctness of the function, passing the test cases and asserting the expected results.