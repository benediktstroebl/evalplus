```python
def triples_sum_to_zero(lst):
    if not any(sum(x) < 0 for x in lst) :
        return True
    else:
        return False
```
This code defines a function triples_sum_to_zero that aims to determine whether the sum of three distinct elements in an input list lst is zero. 

The function begins by using the any() function combined with the built-in function sum() to check if there are no elements in the list whose sum is less than zero. 

If there are no such such elements in the list whose sum is less than zero, the function returns True, indicating that there are three distinct elements in the list whose sum is zero. 

On the other hand, if there are such elements with non-zero sum, the function returns False, which means that the condition for having three distinct elements summing to zero is not met.