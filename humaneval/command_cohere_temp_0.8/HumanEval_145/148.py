```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list according to criteria above
    """
    if not nums:
        return []
    summed_digits = []
    for num in nums:
        sum_ = 0
        for digit in str(num):
            sum_ += int(digit)
        summed_digits.append(sum_)
    sorted_nums = sorted(nums, key=lambda x: (summed_digits.index(sum_), x))
    return sorted_nums
```

This script defines a function `order_by_points` that takes in a list of integers (`nums`). It first checks if the input list is empty, and if so, it returns an empty list. It then proceeds to calculate the sum of digits for each number in the list, storing these sums in the `summed_digits` list. After that, it sorts the `nums` list based on the sum of digits using a lambda function that utilizes the `index` function as the sorting key for ties, followed by the original value. The sorted list is then returned.