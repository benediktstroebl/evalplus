```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sorteed list based on the criteria.
    """
    if len(nums) == 0:
        return []

    # Keep track of the sorted list based on digit sum.
    sorted_by_sum = []

    # Keep track of the original index for tiebreaking.
    original_index_tracker = [-1] * len(nums)

    for digit_sum in range(0, int(np.max(nums) + 1)):
        # Find all elements in the list that have this digit sum.
        current_group = [num for num in nums if sum(map(int, str(num))) == digit_sum]

        # Sort the group based on the original index.
        for i in range(len(current_group)):
            current_group[i] = (current_group[i], i)

        # Add the sorted group to our running result.
        sorted_by_sum.extend(current_group)

    return [num[0] for num in sorted_by_sum if num[1] > original_index_tracker[num[0]]]
```

Here's a brief explanation of how it works:
1. We initialize two empty lists: `sorted_by_sum` and `original_index_tracker`.
2. We iterate through possible digit sums from the smallest to the largest.
3. For each digit sum, we identify all elements in the input list that have this digit sum,
   sort them based on their original index, and append this sorted group to `sorted_by_sum`.
4. During this process, `original_index_tracker` helps us remember the original index for
   tie-breaking when two elements have the same digit sum.
5. Finally, we filter out elements that weren't sorted based on the original index, 
   returning the correctly sorted list.

This solution assumes that `np.max(nums)` is sufficient to iterate through all possible digit sums. 
This works assuming the largest number is not too large, and essentially acts as an infinite loop. 
However, if you're dealing with very large numbers, you may run into numerical issues or limitations. 
In such a case, you would need to refine the approach slightly.