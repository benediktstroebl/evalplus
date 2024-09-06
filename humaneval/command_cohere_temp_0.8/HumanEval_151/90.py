Here's a Python function that solves the given problem and includes explanatory comments:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Input: lst ([1, 3, 2, 0])
    Output: 10
    Explanation: 1 is odd, 3 is odd, 2 is even, 0 is both even and not an integer. sum up: 1^2 + 3^2 + 0 + 0 = 1 + 9 + 0 + 0 = 10
    """
    result = 0
    for num in lst:
        if num % 2 == 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result
```
This function iterates through each element in the input list. If the number is even, not odd, negative, or not an integer, it skips these numbers and does not include them in the sum. The function then returns the sum of the squares of the odd numbers, as explained in the comments. Feel free to add more test cases to ensure the function works correctly for different scenarios!