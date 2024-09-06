```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
	"""
    # Initialize empty lists to keep track of unique and summed elements
    unique = [element for element in l if element not in unique]
    summed = []

    # Iterate through the list
    for element in l:
        if element not in unique:
            unique.append(element)
        else:
            if sum(unique) == 0:
                return True
            else:
                summed.append(element)
                unique = [element]

    # If the list is empty, return False
    return False
```