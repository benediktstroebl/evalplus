Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def double_the_difference(lst):
    odd_squares = sum(x ** 2 for x in lst if x % 2 and x >= 0 and isinstance(x, int))
    return int(odd_squares)
```
This function solves the problem statement by using a sum filter/generator expression to calculate the sum of squares of odd numbers from the list. The function returns 0 if the input list is empty.

To demonstrate the functionality, here is an example:
```python
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))  # Output: 81
print(double_the_difference([0]))  # Output: 0
print(double_the_difference([]))  # Output: 0
```
The function works correctly for the given test cases and returns the expected outputs: 10, 0, 81, and 0 for the respective input lists. 
If an empty list is provided, it returns 0 due to the statement in the prompt:
```
If the input list is empty, return 0.
``` 
Thus, the function handles this scenario appropriately.