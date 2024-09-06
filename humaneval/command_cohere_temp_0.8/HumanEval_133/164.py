```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n**2
    return result
```
This Python script defines a function called sum_squares, which takes a list called lst as input. This function calculates the sum of squared elements in the list and returns the result.

Here's a breakdown of the code within the function:
1. Result initialization: The variable result is initialized to 0. This variable will be used to keep track of the sum of squared elements.
2. For loop: The function uses a for loop to iterate through each element n in the input list lst.
3. Sum of squares: Within the loop, the value of n is squared using the expression n**2. This squared value is added to the result variable using the += operator, updating the total sum of squared elements.
4. Return statement: After processing all elements in the list, the function returns the calculated sum of squared values.

In summary, the sum_squares function takes a list of numbers, squares each number, and adds the squared values together. The result is the sum of squared numbers in the list.