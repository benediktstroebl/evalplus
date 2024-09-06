```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

This Python script defines a function called `sum_squares` that takes in a list of numbers (`lst`) as input. Within the function, it uses a generator expression along with the sum function to calculate the sum of squared integers in the input list. The generator expression iterates through each element `x` in the input list, and for each element, it checks if `x % 1 == 0`, which effectively determines if `x` is a positive integer (since negative numbers and non-integer values will have a different remainder when divided by 1). 

If the condition is met, it squares `x` using the power operator (`**`) and includes it in the sum calculation. Finally, the function returns the computed sum of the squared integers. 

The script does not include any test cases for this function, as it is lacking the necessary test code to fulfill the given instructions completely. It only contains the function definition. To complete the task, test cases should be added to validate the function's behavior against the examples provided in the problem statement. You can add test cases in a separate code block like this:
```python
# Test cases
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, 4, 9]) == 98
assert sum_squares([1, 3, 5, 7]) == 84
assert sum_squares([1.4, 4.2, 0]) == 29
assert sum_squares([-2.4, 1, 1]) == 6
``` 
These test cases cover different scenarios mentioned in the problem statement. Adjust the function if necessary to ensure that it satisfies all test cases.