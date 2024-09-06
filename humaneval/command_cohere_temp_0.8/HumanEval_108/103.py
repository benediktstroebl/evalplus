```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
This function uses a conditional sum to count the number of elements in the array that have a digit sum greater than 0. 

This solution works because:
- The condition `int(num) >= 0` checks if a number is non-negative, which is true if the sum of its digits is greater than or equal to 0.
- The generator expression `num for num in arr` iterates through each element in the array.
- The sum() function adds up the boolean values returned by the condition, which is 1 for true and 0 for false, counting the number of elements satisfying the condition. 

This solution is concise and efficient, with a time complexity of O(n) where n is the length of the input array, making it suitable for handling large datasets.