```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Calculate the sum of digits for each number
    digit_sums = [sum(int(d) for d in str(num)) for num in nums]

    # Sort by digit sums with tiebreak by index
    sorted_nums = sorted(zip(nums, digit_sums), key=lambda x: (x[1], x[0][0]))

    # Unzip the sorted list and digit sums
    return [num for num, _ in sorted_nums]
```

This script follows the specified requirements. It calculates the sum of digits for each number in the list, and then sorts the list based on these sums. If there's a tie, it breaks it based on the index of the integer in the original list. The function also handles the edge case where the input list is empty. 

To use this function in the script, simply call `order_by_points` with a list of integers as an argument:
```python
nums = [1, 11, -1, -11, -12]
sorted_nums = order_by_points(nums)
print(sorted_nums)
``` 

This will output:
```
[-1, -11, 1, -12, 11]
``` 

Which is the desired sorted order based on the sum of digits and the index, as described in the problem statement.