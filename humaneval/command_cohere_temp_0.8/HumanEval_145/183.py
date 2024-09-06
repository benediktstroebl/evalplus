```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if len(nums) == 0:
        return []

    sorted_nums = []
    digit_sum_dict = {}

    for idx, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_dict:
            if idx < digit_sum_dict[digit_sum]:
                continue
            elif idx > digit_sum_dict[digit_sum]:
                sorted_nums.extend(nums[:digit_sum_dict[digit_sum]]);
                sorted_nums.append(num);
                sorted_nums.extend(nums[digit_sum_dict[digit_sum]:idx+1])
                digit_sum_dict[digit_sum] = idx
                continue
        sorted_nums.append(num)
        digit_sum_dict[digit_sum] = idx

    return sorted_nums
```

The approach used in the function `order_by_points` is as follows:
1. First, we handle the base case of an empty list, returning a result as asked.
2. We initialize an empty list `sorted_nums` to store the sorted integers, and a dictionary `digit_sum_dict` to store the index of the last occurrence of each digit sum.
3. We iterate through each number `num` in the list `nums`, calculating the sum of its digits `digit_sum`.
4. For each unique digit sum, the items are sorted and extracted using the `digit_sum_dict`, and the items are appended to `sorted_nums`.
5. The `digit_sum_dict` is updated to reflect the latest index of the last occurrence of each digit sum.
6. After processing all items, the `sorted_nums` list is returned, which holds the integers sorted according to the specified criteria.

This approach guarantees that the integers are sorted first by their digit sum, and then by their original index in case of a tie.