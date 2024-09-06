Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def double_the_difference(lst):
    odd_squares = sum(x**2 for x in lst if x % 2 != 0 and x >= 0 and isinstance(x, int))
    return int(odd_squares)
```
This function leverages Python's list comprehension and the `sum()` function to calculate the sum of squares of odd numbers from the list. The conditions `x % 2 != 0` checks if a number is odd, `x >= 0` checks for positive numbers, and `isinstance(x, int)` ensures the elements are integers. The result is then cast to an integer with `int()` to fulfill the criterion of having a returned integer value.

Here is an example usage of the function:
```python
print(double_the_difference([1, 3, 2, 0]))  # Outputs: 10
print(double_the_difference([-1, -2, 0]))  # Outputs: 0
print(double_the_difference([9, -2]))  # Outputs: 81
print(double_the_difference([0]))  # Outputs: 0
print(double_the_difference([]))  # Outputs: 0
```
This demonstrates the function's behavior for various cases. All outputs will be integers as expected. 
If you wish to test the function with more scenarios, you can add additional test cases to the script. The function is designed to be self-contained and won't need any external dependencies, making it reusable in other parts of your code if needed. 
If you require further customization or have more questions related to the problem, feel free to ask!