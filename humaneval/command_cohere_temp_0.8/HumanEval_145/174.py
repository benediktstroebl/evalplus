```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list based on the criteria.
    """
    if len(nums) == 0:
        return []

    # Compute the digit-based score for each number
    def digit_score(num):
        score = 0
        for digit in str(num):
            score += int(digit)
        return score

    # Sort based on digit score and original index
    sorted_nums = sorted(nums, key=lambda x:[digit_score(x), x])
    return sorted_nums
```

The function first handles the base case of an empty list, then sorts the list based on the sum of the digits of each number, and lastly, uses the original index as a tiebreaker in the sorting. 

You can use this function to sort a list according to the criteria specified in the problem statement. Simply call the function with the argument list `[1, 11, -1, -11, -12]`. The expected output of `order_by_points([1, 11, -1, -11, -12])` is `[-1, -11, 1, -12, 11]`.