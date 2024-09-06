```python
def pairs_sum_to_zero(l):
    return any([x+y == 0 for x,y in zip(l, l[1:])]) and not l[-1] == 0
``` 
The function uses a list comprehension with the any() function to check if there are two elements in the list that sum up to zero. It returns "True" if this condition is met and "False" otherwise.