Here's the solution:

```python
def fizz_buzz(n: int) -> int:
    nums = list(range(0, n))
    return sum(nums.find(7) == num for nums in nums if (nums % 11) != 7 and (nums % 13) != 7)
```

This function uses a list comprehension to count the number of occurrences of the digit 7 in the list of numbers less than n that are divisible by 11 or 13. The function returns 0 if there are no suchs, and returns the count otherwise.