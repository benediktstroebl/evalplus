```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n**2
    
    return result
```
This Python script defines a function called sum_squares, which takes a list of numbers called lst as input. This function calculates the sum of squared numbers in the list and returns the result.

Here's a step-by-step explanation of how the function works:
1. The function starts with a variable result initialized to 0. This variable will be used to keep track of the sum of squared numbers.
2. Then, it iterates through each number n in the input list lst using a for loop.
3. Within each iteration, the current number n is squared by raising it to the power of 2 using the expression n**2.
4. The squared value is then added to the result variable using the += operator. This accumulates the sum of squared numbers.
5. After processing all numbers in the list, the function returns the final value of result, which is the sum of squared numbers.

This script provides a simple and efficient way to calculate the sum of squares of integers in a given list.