```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> l=[1,3,5,-2,1]
    sum=3
    return False
    >>> l=[1,3,5,0]
    sum=0
    return True
    >>> l=[1,2,3,7]
    sum=6
    return False
    >>> l=[2,4,-5,3,9,7]
    sum=10
    return True
    >>> l=[1]
    sum=1
    return False
    ```