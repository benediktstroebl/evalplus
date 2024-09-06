def double_the_difference(nums):
    "Sum of squares of odd integers in a list"
    # Validate input: only consider integers and reject negative values
    filter_pos = filter(lambda x: x > 0 and isinstance(x, int), nums)
    return sum(x**2 for x in filter_pos) ** 2