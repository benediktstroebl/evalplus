Here is a Python script that includes the `pairs_sum_to_zero` function:
```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    """
    return "False" if the list is empty or there is only one distinct pair 
    with sum to zero, else "True" 
    """
    if len(l) == 0:
        return "False"
    for i in range(1, len(l)):
        if l[i] + l[i - 1] == 0:
            return "True"
            break
    return "False"
```

This function takes a list `l` as input and returns "True" if there are two distinct elements in the list that sum to zero, and "False" otherwise. The function uses a simple algorithm to check if there are two distinct elements with a sum of zero. This approach ensures the acceptable performance for lists with a large number of elements.