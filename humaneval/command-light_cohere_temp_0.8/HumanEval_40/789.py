```python
def triples_sum_to_zero(lst):
    # Initialize three variables to track distinct values in lst
    count = 0
    n = len(lst)
    dist = set()

    # Loop through the list
    for num in lst:
        # If the number is already in dist, it's not a triple sum
        if num in dist:
            return False

        # If the number is not in the list yet, add it to dist
        dist.add(num)

        # Increment count
        count += 1

    # Return True if there are three distinct elements that sum to zero
    return count == 3 and lst.
```