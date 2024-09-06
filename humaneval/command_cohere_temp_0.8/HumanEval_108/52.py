```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function sums over all elements in the array `arr` and counts the number of elements where the sum of the digits is greater than 0. It does so by first converting the integer into a string, summing up the values of each digit, and returning `True` if that sum is larger than 0, and `False` otherwise. 

Here is a more detailed outline of the function:
1. Convert each integer `num` in the array to a string, sum up the digits, and check if the sum is larger than 0.
2. Use Python's `sum()` function to add up these boolean values, which will be 0 for False and the index of the element for True.
3. Return the final sum as the answer to the function. 

This code leverages fundamental Python principles such as string manipulation, encapsulation, and modularity. The resulting code is concise and readable, achieving a linear time complexity of O(n). 

This solution sets the foundation for more complex problems involving digitation, modularity, and boolean algebra.