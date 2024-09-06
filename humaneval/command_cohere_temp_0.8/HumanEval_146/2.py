```python
def specialFilter(nums):
    odd_digits = [int(digit) for digit in nums if digit % 2 != 0]
    return sum(num for num in nums if num > 10 and int(num[0]) in odd_digits and int(num[-1]) in odd_digits)
```
This Python script defines a function called `specialFilter` that takes a list of numbers as input. It aims to identify numbers within the list that meet certain criteria:
1. Numbers greater than 10 are considered.
2. Only numbers with odd first digits (first digit > 0) are considered.
3. Only numbers with odd last digits (last digit > 0) are considered.

It then returns the count of numbers that satisfy these conditions. The sum function is used to count the occurrences in the list that meet the defined criteria. The explicit int function usage ensures compatibility with both numeric and string values. The resulting count is returned as the result of the function. 

This solution enables the function to efficiently determine and count numbers that fulfill all the required odd digit conditions while excluding other numbers.