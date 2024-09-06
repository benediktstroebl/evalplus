```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.
    """
    return sum(int(digit) for digit in str(num))

def x_index(num):
    """
    Return the index of the given number in the original list.
    """
    return nums.index(num) if nums else 0

# Test cases
nums = [1, 11, -1, -11, -12]
print(order_by_points(nums) == [-1, -11, 1, -12, 11])
```

This code provides three functions to accomplish the task:
1. `order_by_points(nums)` sorts the list based on the sum of digits with tiebreakers.
2. `sum_of_digits(num)` calculates the sum of digits of a number.
3. `x_index(num)` finds the index of a number in the original list. 

The script also includes test cases to validate its functionality against the given example in the problem statement. 

To run the code, create a `nums` list in local execution and verify if the output matches the expected. 
For example: `print(order_by_points(nums) == [-1, -11, 1, -12, 11])`. 
This will help you check if the function produces the desired sorting result.