```python
def specialFilter(nums):
    odd_digits = [x for x in nums if int(x) > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(odd_digits)
```

This function uses a list comprehension to filter out numbers from the input array that meet the specified criteria - having both first and last digits odd after collapsing the digits into a single integer. The function then returns the length of this filtered list.

To help understand the solution, here's a breakdown of how the function works:
1. **List Comprehension**: The list comprehension `odd_digits = [x for x in nums if int(x) > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]` filters the array `nums`. It examines each element `x` in `nums`, and if the conditions outlined in the problem statement evaluate to True for `x`, it includes `x` in the `odd_digits` list.
2. **Conditional Checks**:
    - `int(x) > 10` checks if the integer version of the digit is greater than 10.
    - `int(str(x)[0]) % 2 == 1` checks if the decimal representation of the first digit, when converted to an integer, yields a remainder of 1 when divided by 2. This digit would be odd.
    - `int(str(x)[-1]) % 2 == 1` checks if the decimal representation of the last digit, when converted to an integer, yields a remainder of 1 when divided by 2. This also ensures that the last digit is odd.
3. **Return Statement**: After the list comprehension has completed, the function returns the length of the `odd_digits` list with the filtered numbers using `return len(odd_digits)`.

This solution adheres to the specified requirements and provides the count of numbers in the input array that meet the given criteria regarding odd digits.