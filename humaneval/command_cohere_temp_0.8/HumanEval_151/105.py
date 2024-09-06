```python
def double_the_difference(lst):
    odd = [x for x in lst if x % 2 != 0 and x >= 0 and isinstance(x, int)]
    return sum(x * x for x in odd)
```
The function `double_the_difference` uses a list comprehension to filter out odd integers from the input list that are also non-negative and integer values. The sum of the squares of these odd numbers is then calculated using a generator expression within the `sum()` function, which efficiently computes the sum without creating the intermediate list. This entire process ensures that only valid odd integers are considered, and if no valid odd integers are present, the function returns 0. 

Here's an example usage:
```python
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))  # Output: 81
print(double_the_difference([0]))  # Output: 0
print(double_the_difference([]))  # Output: 0
```
This function correctly solves the problem as described in the markdown code block. It handles oddness, non-negativeness, and integerness requirements, and also checks for empty lists, returning 0 in such cases.