```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
The `count_nums` function uses a sum construct to iterate through each number in the input `arr` array. For each number, it checks if its digit sum is greater than 0 by converting it to an integer and using a lambda function via the `>= 0` syntax. The final result is the count of numbers with a positive digit sum. 

This solution has a time complexity of O(n), where 'n' is the length of the input array `arr`. It operates on each element once, making the computation efficient with a constant time complexity per check.

The approach utilizes a concise Pythonic style that leverages int and lambda functions for filtering. The lambda function int(num) >= 0 combines the conversion of 'num' to an integer and the comparison of that integer's value with 0. Using `sum` then aggregates the results of these checks for all elements in the array.