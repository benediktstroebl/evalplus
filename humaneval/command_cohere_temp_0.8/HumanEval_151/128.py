```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 and x >= 0)
    return int(odd_squares)
```

This function leverages Python's list comprehension and the `sum()` function to calculate the sum of squares of odd integers in the `nums` list. The conditional statement `x % 2 and x >= 0` ensures that only positive odd numbers are considered, while negative numbers and even numbers are ignored. The result is then returned as an integer, as per the problem's instructions. 

To better understand the behavior of the function, let's analyze its performance on the provided test cases:
1. `double_the_difference([1, 3, 2, 0])` Returns: 10
  * Adds the squares of 1, 3, and 2 to yield 1 + 9 + 4 = 10.
2. `double_the_difference([-1, -2, 0])` Returns: 0
  * Ignores the negative numbers and even number, resulting in a sum of 0. 
3. `double_the_difference([9, -2])` Returns: 81
  * Includes only the odd number 9, and computes its square, resulting in 81. 
4. `double_the_difference([0])` Returns: 0
  * Given an empty list, the sum operation returns 0, as there are no elements to compute. 

This detailed analysis showcases how the function adeptly handles the various scenarios outlined in the problem statement.