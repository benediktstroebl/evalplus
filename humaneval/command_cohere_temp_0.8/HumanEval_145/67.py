```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # List of tuples: sort keys [digit_sum, original_index]
    sort_keys = list(zip(digit_sums, range(len(nums))))

    # Sort by sum-of-digits (with tiebreaks decided by original index)
    sorted_nums = sorted(nums, key=lambda n: sort_keys[nums.index(n)])

    return sorted_nums
```
This code will sort the given list as per the specified conditions. It calculates the sum of digits for each number, creating a list of these sums, and then ties breaks by using the original index. The list is sorted using the custom key function that feeds the original number's index to the sort keys list. This will ensure the numbers with similar digit sums sort in the intended order.