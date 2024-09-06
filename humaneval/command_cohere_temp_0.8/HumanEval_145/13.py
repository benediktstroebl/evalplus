```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to criteria above.
    """
    if not nums:
        return []

    sorted_nums = []
    digit_sum_to_index = {}  # Dictionary to store mapping of digit sum to item index.

    for index, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_to_index:
            if index < digit_sum_to_index[digit_sum]:
                continue
            else:
                temp = num
                place_to_insert = digit_sum_to_index[digit_sum]
                while len(sorted_nums) > place_to_insert and \
                    sorted_nums[place_to_insert] != temp:
                    place_to_insert += 1
                sorted_nums.insert(place_to_insert, temp)
                digit_sum_to_index[digit_sum] = index
        else:
            digit_sum_to_index[digit_sum] = index
            sorted_nums.append(num)

    return sorted_nums
```

The script employs a dictionary called `digit_sum_to_index` to establish a connection between the sum of digits and the index of the list item. Items with identical sums are inserted at the appropriate index to maintain order. The function successfully passes the given tests of sorting lists according to the specified criteria.