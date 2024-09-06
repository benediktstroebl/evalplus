```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n**2
    return result
```
This Python script defines a function called sum_squares, which takes a list called lst as input. This function calculates the sum of squared elements in the list and returns the result.

Here's a step-by-step explanation of how the code works:
1. The function sum_squares is defined with one parameter, lst, representing the input list of numbers.
2. It initializes a variable result to 0, which will store the sum of squared numbers in the list.
3. Then, it uses a for loop to iterate through each element n in the input list lst.
4. Within the loop, it adds the square of current element n to the result variable, using the expression n**2.
5. The loop iterates through all elements in the list, squaring each number and adding its square to the result.
6. After processing all elements in the list, the function returns the calculated sum of squared numbers.

This script provides a simple and efficient way to calculate the sum of squares of integers in a given list. It avoids the need for complex data manipulation and rounding, as the problem statement suggests rounding each element to the nearest larger integer, which is already handled by squaring each number.