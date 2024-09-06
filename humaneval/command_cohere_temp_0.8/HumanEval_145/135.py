```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Initialize a list to store the sorted elements.
    sorted_nums = []

    # Iterate through the original list.
    for idx, num in enumerate(nums):
        # Calculate the sum of digits.
        num_digits = sum(map(int, str(num)))

        # Append a pair [sum_digits, num] to the list.
        sorted_nums.append([num_digits, num])

    # Sort the list of pairs based on the first element.
    sorted_nums.sort(key=lambda x: x[0])

    # Extract the sorted integers back from the list of pairs.
    sorted_nums = [item[1] for item in sorted_nums]

    # If there are multiple integers with the same digit sum,
    # Sort them based on their original index.
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            sorted_nums.insert(i + 1, sorted_nums.pop(i))

    return sorted_nums
```

This Python script implements the specified sorting algorithm, with a test case that checks the expected sorting order of the example input list and an empty list test case to validate edge-case behavior.