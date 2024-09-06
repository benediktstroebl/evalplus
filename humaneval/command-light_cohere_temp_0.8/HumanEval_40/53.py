```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # Initialize variables and check length
    if len(l) != 3: return False

    # Initialize variables to keep track of the three largest
    #  elements and their sum
    max_1 = float('-inf')
    max_2 = float('-inf')
    max_3 = l[0]
    sum_1 = l[0]
    sum_2 = l[1]
    sum_3 = l[2]

    # Check for three distinct elements that sum to zero
    for i in range(1, len(l)):
        if l[i] > max_3:
            max_3 = l[i]
        if l[i] > max_2:
            max_2 = l[i]
        if l[i] > max_1:
            max_1 = l[i]
        sum_1 += l[i]
        sum_2 += l[i]
        sum_3 += l[i]

    # If all three largest elements sum to zero, return True
    if max_1 + max_2 + max_3 == 0:
        return True
    return False
```