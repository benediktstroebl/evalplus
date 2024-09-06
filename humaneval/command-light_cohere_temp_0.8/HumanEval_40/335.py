```python
def triples_sum_to_zero(lst):
    """
    Function to check if there are three distinct elements sum of which is zero in a list.
    """
    sum(sum(lst[:3]))
    """
    return "Yes" if (len(lst)==3 and all(x+y+z==0 for x,y,z in zip(lst[:3])) else "No"
```