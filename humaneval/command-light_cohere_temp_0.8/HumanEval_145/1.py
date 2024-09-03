```python
def order_by_points(nums):
    # Initialize empty list to store the sorted numbers
    sorted_nums = []

    # Sort the list of integers based on digit sum
    for num in nums:
        # Convert to string to get the sum of its digits
        sumstr = str(num)[::-1]
        digit_sum = sum(int(char) for char in sumstr)

        # Add the number to the list if its digit sum is less than the previous one
        if digit_sum < sorted_nums[-1]:
            sorted_nums.append(num)
        else:
            pass

    # Return the sorted list
    return sorted_nums
```