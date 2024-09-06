```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers with no explicit upper bound.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    # Make copies of the lists to avoid modifying the original list.
    nums_copy = nums.copy()
    digit_sums = [sum(int(d) for d in str(n)) for n in nums_copy]
    index_sorts = [nums.index(n) for n in nums_copy]

    # Sort by sum of digits with tiebreaks.
    sorted_idx = sorted(range(len(nums)), key=lambda i: [digit_sums[i], index_sorts[i]])

    return [nums_copy[idx] for idx in sorted_idx]
```

The function proceeds by first creating copies of the original list (`nums_copy`) and the list of digit sums (`digit_sums)). This is done to avoid modifying the original list which could compromise the integrity of the algorithm's results, as well as to prevent potential errors when working with the original list. 

The creation of `index_sorts` is crucial to break ties between integers with the same digit sum. It provides a way to sort integers according to their original positions in `nums`. 

The final line sorts the indices of the numbers based on their digit sums and their original positions, using a lambda function as the sorting key. The lambda function uses a list of the digit sum and the index as the key, ensuring that integers with the same digit sum are sorted according to their original list position. 

Ultimately, the function returns a sorted list of integers based on the criteria. 

This approach provides an effective solution to the problem, leveraging Python's sorting capabilities while ensuring a deterministic outcome.