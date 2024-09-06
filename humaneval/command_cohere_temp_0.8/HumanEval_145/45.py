```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True

    Returns:
        List: Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        (int) num: Number whose digit sum needs to be calculated.

    Returns:
        int: Sum of digits of the given number.
    """
    return sum(int(digit) for digit in str(num))

def x_index(num):
    """
    Identify the index of the given number in the original list.

    Args:
        (int) num: Number whose index needs to be determined.

    Returns:
        int: Index of the number in the original list.
    """
    return nums.index(num) if nums.count(num) == 1 else -1
```

This code block includes three separate functions to achieve the desired result:
1. `order_by_points(nums)` executes the main task of sorting the integer list according to the described criteria. It first checks if the input list is empty, returning an empty list if so. It then sorts the list by passing a lambda function as the key argument, leveraging the `sum_of_digits()` and `x_index()` functions to determine the sorting order.
2. `sum_of_digits(num)` calculates the sum of the digits of a given number, achieved by iterating through the digits of the string representation of the number and summing them.
3. `x_index(num)` identifies the original index of a given number in the list, utilizing the `index` method to find the index if the number occurs only once in the list, or returning -1 if not found or duplicated.

This code aims to sort a list of integers based on the sum of their digits, with tiebreakers being their original index. Adaptations are made to address potential issues like empty lists or lists with duplicate entries.