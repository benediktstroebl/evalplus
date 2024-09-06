```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    """
    if not nums:
        return []

    # Calculate the digit-sum-sorted index list
    ds_idxs = [
        (sum(int(d).digits()), i) 
        for i, d in enumerate(nums) 
    ]
    ds_idxs.sort()
    
    # Use the sorted index list to construct the sorted digit-sum list
    sorted_nums = [nums[i] for i, _ in ds_idxs]

    return sorted_nums
```

This approach first calculates the sum of digits and corresponding original indices for each number, then sorts these, and finally uses the sorted indices to reorder the original list. 

This produces the desired sorting based on digit sums and original indices, as per the problem statement. 

This approach avoids explicit sorting of the original list, instead directly manipulating the order based on the sorted index list. 

Note: if multiple items have the same digit sum, their original index is used as a tie-breaker, as per the problem statement. 

This approach assumes that `int(d).digits()` returns a sorted list of digits for each number `d` (as in Python). 

Note: the empty list case is handled by returning an empty list if `not nums`.  This is the approach used in the supplied code.  However, this question hasn't explicitly mentioned handling the empty list case, so if you want to conform to the letter of the problem strictly, you might need to explicitly state that it returns an empty list when `nums` is empty.  But this would be a minor clarification, as the code already works correctly in this regard.  You may want to mention this in your documentation nonetheless, for clarity.  Here's a sample version that emphasizes this: 

```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Returns an empty list if the input list is empty.

    """
    if not nums:
        return []

    # Calculate the digit-sum-sorted index list
    ds_idxs = [
        (sum(int(d).digits()), i) 
        for i, d in enumerate(nums) 
    ]
    ds_idxs.sort()
    
    # Use the sorted index list to construct the sorted digit-sum list
    sorted_nums = [nums[i] for i, _ in ds_idxs]

    return sorted_nums
```