```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which we calculate the sum of digits.

    Returns:
        int: Sum of digits of the given number.
    """
    sum_so_far = 0
    num_str = str(num)
    for digit in num_str:
        sum_so_far += int(digit)
    return sum_so_far

def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for which we determine the index.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1

# Test cases
nums = [1, 11, -1, -11, -12]
print(order_by_points(nums) == [-1, -11, 1, -12, 11])

nums = [1, 5, 10, 50, 51, 55, 551, 555]
print(order_by_points(nums) == [1, 5, 5, 50, 51, 55, 551, 555])

nums = [1, 4, 3, 4, 3, 2, 2, 1]
print(order_by_points(nums) == [1, 1, 2, 2, 3, 3, 4, 4])

nums = []
print(order_by_points(nums) == [])
```

This code provides the `order_by_points` function with three supporting functions: `sum_of_digits`, which calculates the sum of the digits of a number; `x_index`, which determines the index of a number in the original list; and various test cases to validate the functionality of the `order_by_points` function. 

Let's break down the code:
1. `sum_of_digits(num)`: This function takes an integer `num` as input and calculates the sum of its digits. It converts the integer to a string `num_str`, iterates over each digit, and adds them up in the `sum_so_far` variable. Finally, it returns the calculated sum.
2. `x_index(num)`: This function determines the index of the given number `num` in the original list `nums`. It uses the `index` method of the list to find the index of the `num`. However, there's a caveat: this function assumes that the list `nums` is already sorted. If it's not sorted, the function returns `-1` as a fallback value.
3. Test cases: There are three test cases provided to validate the behavior of the `order_by_points` function. These test cases showcase a variety of scenarios, including empty lists, and sorted lists with different