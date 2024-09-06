```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n ** 2
    return result
```
This function defines a Python function called sum_squares that takes a list called lst as input. It calculates the sum of squared elements in the list using a for loop, where each element n in the list is squared (n ** 2) and the results are summed together. The function returns the final sum of the squared numbers.

Here is an example of how to use the function:
```python
my_list = [1, 4, 9, 16, 5, 6, 7]
result = sum_squares(my_list)
print(result)  # Output: 276
```
This demonstrates how to use the `sum_squares` function with a sample input list my_list, calculating the sum of squares of its elements, and the resulting output is 276.