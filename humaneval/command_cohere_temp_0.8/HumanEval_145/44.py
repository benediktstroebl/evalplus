```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list based on the criteria.
    """
    if not nums:
        return []

    # Helper function to compare two numbers with sum-of-digits tiebreaker.
    def compare(a, b):
        if sum_digits(a) != sum_digits(b):
            return sum_digits(a) - sum_digits(b)
        return idx(a) - idx(b)

    # Sort the list based on the sum-of-digits criteria.
    nums.sort(key=lambda x: (sum_digits(x), idx(x)))

    return nums


# Helper function to calculate the sum of digits for a given number.
def sum_digits(n):
    return sum(int(d) for d in str(n))


# Helper function to get the index of a number in the original list.
def idx(n):
    return nums.index(n) if n in nums else len(nums)
```

This code provides a `compare` function as a tiebreaker for sorting,
where it first compares the sums of digits and then falls back to the original index of the numbers in the list. 

The `sum_digits` function calculates the sum of digits for a given number,
while the `idx` function determines the index of a number within the original list. 

The `order_by_points` function applies the sorting algorithm to the input list,
using the sum-of-digits and original index as key criteria for sorting. 

This approach ensures that numbers with the same sum of digits are sorted based on their original positions in the list. 

Feel free to adapt this code to your needs or explore the reasoning behind the sorting algorithm in more detail! Let me know if you would like to further clarify any of the steps taken to solve the problem.