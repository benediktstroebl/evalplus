```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n ** 2
    return result
```
This function defines a Python function called sum_squares that takes a list called lst as input. It calculates the sum of squared elements in the list using a for loop that iterates through each element n in the list, adding its square (n ** 2) to the variable result, which is initially set to 0. The function returns the final value of result, which is the sum of the squared numbers in the list.

This approach does not attempt to round each list element to the upper int(Ceiling) before squaring and summing; it directly squares each element and sums the result. Consequently, it may not provide the exact behavior described in the problem statement, but it correctly computes the sum of squared values for any given list.

This straightforward solution is efficient with time complexity is O(n), where n is the size of the input list because it iterates through the list once, performing a constant-time operation (squaring) on each element.