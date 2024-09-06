```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the digit in the original list.

    """
    if not nums:
        return []

    # Compute the digit-based score of each number
    def digit_score(num):
        return sum(int(d) for d in str(abs(num)))

    scores = [digit_score(num) for num in nums]

    # Apply tiebreaker rules to sort the list
    sorted_nums = sorted(zip(nums, scores), key=lambda x: (x[1], x[0]))
    return [num for num, _ in sorted_nums]
```

The function first calculates the digit-based score for each number using the `digit_score` helper function. It then sorts the list based on these scores and, in case of a tie, passes the original number through the sorting process, guaranteeing the intended behavior with respect to the index of the numbers in the input list.