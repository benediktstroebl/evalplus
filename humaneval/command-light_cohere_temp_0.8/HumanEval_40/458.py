```python
def triples_sum_to_zero(lst):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    triple list with elements: {1, 3, 5, 0}
    """
    return sum(set(map(lambda x: x, lst))) == 0

# Test the function
if triples_sum_to_zero([1, 3, 5, 0]):
    print("It's possible to have three distinct elements in the list that sum to zero.")
else:
    print("It's not possible to have three distinct elements in the list that sum to zero.")

 triple list with elements: {1, 3, -2, 1}
"""

if triples_sum_to_zero([1, 2, 3, 7]):
    print("It's possible to have three distinct elements in the list that sum to zero.")
else:
    print("It's not possible to have three distinct elements in the list that sum to zero.")

 triple list with elements: {2, 4, -5, 3, 9, 7}

```