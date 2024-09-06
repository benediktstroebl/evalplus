```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    list of integers is passed in and converted to a list.
    if sum(l) == 0:
        return "List contains three distinct elements that sum to zero."
    else:
        return "Not three element sum to zero"
```