```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
	"""
    # Initialize variables
    min = float('inf')
    seen = set()
    for num in l:
        # If the current number is a new element and the sum is not yet zero
        if num in seen and num != 0 and num + seen.sum() > 0:
            return False
        seen.add(num)
        # If the sum of the seen elements is now zero, add the seen elements to the result list
        result = [num for num in seen] + result
        return result
```