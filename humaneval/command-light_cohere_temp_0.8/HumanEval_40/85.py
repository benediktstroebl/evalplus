```python
def triples_sum_to_zero(l):
    """
    checks whether the list of integers has three distinct elements that sum to zero.
    return: True if valid, False otherwise
    """
    # Sort the list to make sure that the loop can detect duplicates
    l.sort(sorted())
    # Initialize a counter for distinct sums to zero
    sum_counter = 0
    for num in l:
        # Initialize the sum of the current element and the previous sum
        sum = num
        previous_sum = sum_counter
        # Add the current element to the sum and increment the counter
        sum += num
        sum_counter += 1
    # If the sum counter is 3, it means we found three distinct elements that add up to zero.
    return: sum_counter == 3
    return True
```