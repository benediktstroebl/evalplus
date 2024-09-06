```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to criteria above.
    """
    if len(nums) == 0:
        return []

    # Calculate the sum of digits for each number in the list.
    total_digits = [sum(map(int, str(n))) for n in nums]

    # Tiebreak decisions are made in case of identical digit sums:
    sorted_nums = sorted(zip(nums, total_digits), key=lambda x: (x[1], x[0][0]))

    # List of integers after sorting by digit sum.
    sorted_by_digit_sum = [num for digit_sum, num in sorted_nums]

    # Finally, the list is sorted in increasing order of digit sum,
    # with tiebreak decisions based on the index of the integer in the original list.
    return sorted_by_digit_sum
```

This script sorts the list `nums` based on the sum of the digits of each number in the list. If multiple numbers have the same digit sum, the list is further ordered based on the index of the number in the original list. The result is returned as a new list. An empty input list returns an empty output list.

Let's break down the code step by step:
1. **Handling an Empty List:**
   ```python
   if len(nums) == 0:
       return []
   ```
   This condition checks if the input list is empty. If it is, the function returns an empty list `[]` directly. This is the base case of the recursive function and prevents any further processing from being done.

2. **Calculating the Sum of Digits for Each Number:**
   ```python
   total_digits = [sum(map(int, str(n))) for n in nums]
   ```
   This line uses a list comprehension to calculate the sum of the digits for each number (`n`) in the input list (`nums`). `sum(map(int, str(n)))` calculates the sum of the digits in the string representation of the number `n`. This is a line that calculates the `total_digits` list that represents the sum of the digits for each number in the list.

3. **Sorting the Numbers Based on Digit Sum and Index:**
   ```python
   sorted_nums = sorted(zip(nums, total_digits), key=lambda x: (x[1], x[0][0]))
   ```
   This line sorts the list of pairs `(n, digit_sum)` using the `sorted` function. The `zip` function transforms the list of numbers `nums` and the list of corresponding digit sums `total_digits` into a list of pairs. The `key` parameter defines a lambda function `(lambda x: (x[1], x[0][0]))` that specifies the sorting order. `x[1]` sorts the pairs in descending order based on the digit sum. If the digit sum is the same, `x[0][0]` sorts the pairs in ascending order based on the index of the number in the original list. The result is a list of pairs `(num, digit_sum)` sorted according to the criteria specified in the problem.

4. **Creating the Output List:**
   ```python
   sorted_by_digit_sum