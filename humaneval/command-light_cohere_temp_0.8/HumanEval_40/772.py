```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    """

    # Initialize variables
    current, target = 0, 0
    seen = set()

    # Loop through list
    for num in l:
        if current + num in seen:
            return False

        seen.add(num)
        current += num

        # Check if current sum to 0
        if current == target:
            return True

        target += 3

    return False
```