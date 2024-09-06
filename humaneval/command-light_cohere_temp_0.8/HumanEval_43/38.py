```python
def pairs_sum_to_zero(l):
    """
    Function to check whether there are two elements in a list that sum to zero.
    """
    returns: True if there are two distinct elements in the list that sum to zero, and False otherwise.
    """
example usage:
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Initialize a set to store the values of the list
    set_values = set(l)

    # Initialize two variables to store the first and last elements of the list
    first_el = l[0]
    last_el = l[-1]

    # Loop through the list
    for num in l[1:]:

        # Check if the current element is in the set
        if num in set_values:
            continue

        # If the current element is not in the set, add it
        set_values.add(num)

        # Check if the sum of the current element and the previous element is zero
        if first_el + num == last_el:
            set_values.remove(first_el)
            break

    # Return True if there are two distinct elements that sum to zero, and False otherwise
    return set_values.isdisjoint()

```