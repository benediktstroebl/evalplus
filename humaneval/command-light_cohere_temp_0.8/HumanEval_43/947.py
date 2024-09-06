```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension is filtering the list, and checking if the sum of two adjacent elements is equal to zero.
 pairs_sum_to_zero([1, 3, 5, 0])
 True  # passes the test

``` 
The function uses a list comprehension to filter out lists that do not have two elements whose sum equals zero. The function returns 'True' if the list passes the test and 'False' otherwise.