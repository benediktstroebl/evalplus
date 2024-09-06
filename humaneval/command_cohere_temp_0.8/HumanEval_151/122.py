Here's a Python script that contains a function named `double_the_difference` which solves the problem as per the given markdown code block:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result
```

The function `double_the_difference` takes a list of numbers as an argument and returns the sum of the squares of odd numbers in the list, while ignoring any negative numbers or non-integer values. To achieve this, it iterates through each number in the input list. If the number is odd, positive, and an integer, it gets added to the total sum of squares (`result`). The function then returns this total.

To test this function, you can call it with a variety of input lists, such as:
```python
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))  # Output: 81
print(double_the_difference([0]))  # Output: 0
```

The function will indeed return the expected outputs based on the problem statement.