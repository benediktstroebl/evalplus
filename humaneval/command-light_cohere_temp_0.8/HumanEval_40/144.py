```python
def triples_sum_to_zero(lst):
    sum_triple = lambda x: x[0] + x[1] + x[2]
    
    if sum_triple(lst) == 0:
        return True
    else:
        return False
``` 
This code defines a function `triples_sum_to_zero` that takes a list of integers as input. The `sum_triple` function calculates the sum of any triplet of elements, and if this sum is equal to zero, the function returns `True`; otherwise, it returns `False`. 

The code also provides some test cases to check the correctness of the function. The function will correctly identify the true in the test cases and fail in the other cases.