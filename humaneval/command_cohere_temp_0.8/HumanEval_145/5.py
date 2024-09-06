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

    # List of tuples: sort key is the sum-of-digits score, tiebreak is the index in the original list
    sorted_nums = sorted(zip(digit_sums, nums), key=lambda x: x[0], reverse=False)

    # Extract the sorted integers list
    return [n for _, n in sorted_nums]
```

This code calculates the sum of the digits of each number in the list, pairs each sum with its corresponding number, and then sorts these tuples. The sorting is done using the `key` parameter, which specifies a function that transforms the tuple into a sorting key. We use a lambda function (`lambda x: x[0]`) to sort by the first element of the tuple (i.e., the sum-of-digits score).

Finally, we extract the sorted integers back from the sorted tuples using a list comprehension and return the result. This algorithm avoids unnecessary sorting of the original list, which could lead to inefficiencies for large lists, and provides a reasonable solution in terms of time and space complexity.