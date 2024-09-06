```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # Ensure the list is not empty
    if not nums:
        return []

    # Convert the list to strings for easier manipulation
    num_strings = [str(num) for num in nums]

    # Calculate the sum of digits for each number and sort by this value
    sorted_by_sum = sorted(num_strings, key=lambda x: sum(char.isdigit() and int(char) or 0 for char in x))

    # Extract the original list elements using the sorted strings
    sorted_nums = [int(str_num) for str_num in sorted_by_sum]

    # Further sort in the case of ties, using the index in the original list
    sorted_nums.sort(key=lambda num: (num, nums.index(num)))

    return sorted_nums
```

This approach first converts the list of integers to strings, which allows us to easily manipulate the digits. We calculate the sum of the digits for each number and sort the strings accordingly. Then, we extract the original list elements from the sorted strings using `int(str_num) for str_num in sorted_by_sum` and use a key function `(lambda num: (num, nums.index(num)))` for sorting to introduce a secondary sort key in case of ties. This key will sort the numbers based on their value and finally, their index in the original list.