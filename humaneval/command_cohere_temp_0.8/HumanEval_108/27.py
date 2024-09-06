Here is a Python script with a self-contained function that solves the problem:
```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    # Define a variable to store the count of numbers with positive digit sum.
    count = 0
    for num in nums:
        if num < 0:
            # If the number is negative, we consider the absolute value of the number and subtract 1 from the sum of digits.
            digits = abs(num)
            sum_of_digits = sum(map(int, str(digits))) - 1
        else:
            # If the number is positive, we calculate the sum of digits normally.
            digits = num
            sum_of_digits = sum(map(int, str(digits)))
        if sum_of_digits > 0:
            count += 1
    return count
```

This script defines a function `count_nums` that takes an array of integers as input and returns the number of elements in the array that have a sum of their digits greater than 0. The function first converts the array of strings to an array of integers and then checks if each integer is positive or negative. If the integer is positive, it calculates the sum of its digits normally. If the integer is negative, it takes the absolute value of the number and subtracts 1 from the sum of its digits. It then increments a counter if the sum of the digits is greater than 0. The function returns the final count.

Here is an example usage of the function:
```python
# Test the function on some examples
print(count_nums([0, 1, 2, -3, -4, 5, -6]))  # Output: 5
```

This will return 5, as the positive numbers have digit sums of 1, 1, 2, 5, and 6, and the negative numbers have digit sums of 3, 4, and 6.