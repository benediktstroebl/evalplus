Here's a Python script that contains a function named `double_the_difference` which solves the problem statement mentioned above:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result

# Test cases
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 50
    assert double_the_difference([-2, -4, -6, -8]) == 0
    assert double_the_difference([]) == 0

test_double_the_difference()
```

This script defines the `double_the_difference` function and uses a for loop to iterate through each number in the input list. If the number is odd, not negative, and an integer, it gets added to the total sum. The test_double_the_difference function provides test cases to ensure the function `double_the_difference` returns the expected outputs.

Let's break down the code step by step:
1. **Function Definition**:
   ```python
   def double_the_difference(lst):
       """
       Given a list of numbers, return the sum of squares of the numbers
       in the list that are odd. Ignore numbers that are negative or not integers.
       """
       ...
   ```
   This part defines the function `double_the_difference` that takes one parameter `lst`, which is the list of numbers as input. The docstring provides a description of the function's purpose.
2. **Iteration and Validation**:
   ```python
   for num in lst:
       if num % 2 == 0 and num >= 0 and isinstance(num, int):
           result += num ** 2
   ```
   Here, we use a for loop to iterate through each `num` in the input list `lst`. We check if the `num` is even (because odd numbers won't have a remainder when divided by 2), non-negative (using the `>=` operator), and an integer (using the `isinstance` function). If all these conditions are met, we add `num` squared (`num ** 2`) to the `result` variable.
3. **Return Statement**:
   ```python
   return result
   ```
   After iterating through all numbers in the list, the function returns the computed sum of squares of odd non-negative integers.
4. **Test Cases**:
   ```python
   def test_double_the_difference():
       assert double_the_difference([1, 3, 2, 0]) == 10
       assert double_the_difference([-1, -2, 0]) == 0
       assert double_the_difference([9, -2]) == 81
       assert double_the_difference([0]) == 0
       assert double_the_difference([2, 4, 6, 8]) == 50
       assert double_the_difference([-2, -4, -6, -8]) == 0
       assert double_the_difference([]) == 0
   ```
   This part defines a function `test_double