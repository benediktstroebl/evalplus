```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 == 1 and x >= 0)
    return int(odd_squares)
```

This function calculates the `sum(x**2 for x in nums if x % 2 == 1 and x >= 0)`, which is the sum of squares of odd integers up to and including the largest odd number, and returns the result as an integer if there are any, or none if the list is empty or contains only even or negative numbers. 

Here is an example usage of the function:
```python
print(double_the_difference([1, 3, 2, 0]))  # 10
print(double_the_difference([-1, -2, 0]))  # 0
print(double_the_difference([9, -2]))  # 81
print(double_the_difference([0]))  # 0
print(double_the_difference([]))  # 0
``` 

The function passes the given test cases and will return the sum of squares of odd numbers in the list and returns 0 if the list is empty or contains even or negative numbers.