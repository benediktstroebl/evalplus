```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list according to criteria above
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number
    """
    numstr = str(num)
    return sum(int(digit) for digit in numstr)

def x_index(num):
    """
    Detect the index of the given number in the original list
    """
    return nums.index(num) if nums != [] else -1

# Test Cases
nums = [1, 11, -1, -11, -12]
print(order_by_points(nums) == [-1, -11, 1, -12, 11]) # Should print True

nums = [1, 5, 51, 55, 505]
print(order_by_points(nums) == [1, 5, 51, 55, 505]) # Should print True

nums = []
print(order_by_points(nums) == []) # Should print True
```

This script provides three functions:
1. `order_by_points(nums)` sorts the given list based on the sum of digits with tiebreaks, as described in the prompt.
2. `sum_of_digits(num)` calculates the sum of the digits of a number, which is used as the primary sorting criteria.
3. `x_index(num)` determines the original index of a number, which is used for tiebreak.

The final section provides test cases that verify the function `order_by_points` performs as expected. 

I hope this assists with your self-contained Python solution. Let me know if you have any additional questions!