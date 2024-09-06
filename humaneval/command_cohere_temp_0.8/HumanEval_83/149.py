```python
def starts_one_ends(n):
    pos_int = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if n < 1 or n > 10:
        return 0
    if n == 1:
        return 1
    return sum(1 for x in range(n-1, 0, -1) if pos_int[x] == '1' or pos_int[n-x-1] == '1')
```
The function `starts_one_ends()` will return the count of numbers that have a given `n` number of digits, and that either start or end with the digit 1. This is done using a list comprehension that cycles through `n` digits, and checks if the first digit in the string is 1, or if the last digit in the string is 1 (if `x` is the first index of the number, then `n-x-1` is the last index of the number). The function returns 0 if `n` is less than 1 or greater than 10, and returns 1 if `n` is 1, as mentioned in the prompt. You can test the function using `pytest`. 
Let's breakdown the solution step by step:
1. We define a list `pos_int` that contains all single-digit positive integers.
2. We handle edge cases where n is less than 1 or greater than 10, returning 0 in these cases.
3. If `n` is equal to 1, it is the only number that starts and ends with 1, so we return 1.
4. For all other values of n, we use a list comprehension to iterate over decreasing values of `x`, from `n-1` down to 1.
5. For each `x`, we check if the `x`th digit of the number (from the right) is equal to '1', which indicates that the number ends with 1. Alternatively, we check if the (`n-x-1`)th digit of the number (from the left) is equal to '1', which indicates that the number starts with 1.
6. We sum up the values 1 for all valid `x`, which gives the count of numbers that start or end with 1 within `n` digits. 

The solution is efficient because it takes linear time in `n` and can be readily adapted to solve a variety of similar problems involving counting numbers with specific characteristics in a given range. 
If there is anything else I can help with, let me know!