Here's a self-contained Python function that sorts a list of integers in ascending order based on the sum of their digits:
```python
def order_by_points(nums):
    # Initialize a list to store the sorted output
    sorted_nums = []

    # Calculate the sum of each digit in the number
    for num in nums:
        sum_digit = sum(int(c) for c in str(num))

    # Sort the list based on the sum of digits in ascending order
    for i in range(len(nums)):
        # Find the index of the current number with the highest sum of digits
        index = nums.index(sum_digit)
        # If the index is not within the bounds of the new list, ignore that element
        if index < 0 or index >= len(sorted_nums):
            continue
        # Move the current number to the correct index in the new list
        sorted_nums.insert(sorted_nums.pop(index) )

    return sorted_nums
```

This function works by first calculating the sum of each digit in each number in the input list. Then, it sorts the list based on these digit sums in ascending order. Finally, it returns the list of numbers that have been sorted.