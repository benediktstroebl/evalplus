```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    sorted_nums = []
    digit_sum_dict = {}

    for idx, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_dict:
            if idx < digit_sum_dict[digit_sum]:
                continue
            else:
                temp = nums[digit_sum_dict[digit_sum]]
                nums[digit_sum_dict[digit_sum]] = num
                nums[idx] = temp
        digit_sum_dict[digit_sum] = idx
        sorted_nums.append(num)

    return sorted_nums
```

The function `order_by_points` sorts a list of integers based on the sum of their digits, and in case of a tie, it decides the order based on the index of the integer in the input list. The function initializes an empty list `sorted_nums` and a dictionary `digit_sum_dict` to store the sum of digits and their corresponding indices. It then iterates through each number in the input list, calculates the sum of its digits, and checks if the sum already exists in the `digit_sum_dict`. If it does, the function compares the index of the current number with the index stored in the dictionary to break the tie; if the index of the current number is smaller, it skips the number and leaves the previous number in the sorted list. Otherwise, it swaps the numbers in the `nums` list and updates the dictionary to reflect the new index. Finally, it adds the number to the `sorted_nums` list, which returns at the end as an ordered list according to the specified criteria.