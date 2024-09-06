```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n ** 2
    return result
```
This Python script defines a function called sum_squares, which takes a list called lst as input. This function calculates the sum of squared elements in the list and returns the result.

Here's a breakdown of the code within the function:
1. Result initialization: The variable result is initialized to zero. This variable will be used to accumulate the sum of squared numbers in the list.
2. Loop through the list: The function performs a loop over each element in the input list using a for loop. The loop variable n represents the current element in the list.
3. Squaring each element: Within the loop, the value of n is squared using the exponentiation operator (**) to calculate the square of the current element. This squared value is then added to the result variable using the += operator.
4. Returning the result: After processing all elements in the list, the function returns the value of the result variable, which now holds the sum of squared values.

In summary, the code iterates over each element in the input list, squares it, and adds the squared value to the result variable. Finally, the function returns the accumulated result, which provides the sum of squared numbers in the input list.