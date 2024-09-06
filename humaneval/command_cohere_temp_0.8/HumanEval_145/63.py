```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list according to specified criteria
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given integer

    Args:
        num (int): Number

    Returns:
        int: Sum of digits of the given number
    """
    return sum(int(d) for d in str(num))

def x_index(num):
    """
    Determine the index of the given number in the original list

    Args:
        num (int): Number

    Returns:
        int: Index of the number in the original list
    """
    return nums.index(num) if nums != [] else 0
```

This script includes three separate functions to tackle the prompt:
1. `order_by_points(nums)` takes the input list and sorts it based on the sum of its digits, using a lambda function as the sorting key. It also incorporates a tiebreaker that assigns elements with the same digit sum to their original index.
2. `sum_of_digits(num)` calculates the total of a number's digits by iterating through its decimal representation.
3. `x_index(num)` identifies the original index of a specific element, leveraging the list `nums` to find the position if the list is not empty. If the list is empty, it defaults to 0. 

You can use these functions in conjunction to solve the problem and gain more insight into the sorting mechanism.