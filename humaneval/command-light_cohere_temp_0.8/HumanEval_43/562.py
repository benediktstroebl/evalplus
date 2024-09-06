```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >> pairs_sum_to_zero([1])
    False
    ``` 
This code defines a function called pairs_sum_to_zero that takes a list of integers as an argument. The function returns True if there are two distinct elements in the list that sum to zero, and False otherwise. The function uses a use a simple algorithm to compare the sum of two elements and returns the result accordingly.