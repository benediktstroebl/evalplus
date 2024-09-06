```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function sums over all elements in the array `arr` and counts the number of elements where the sum of the digits is greater than 0. The output of this function should match the expected outputs in the docstring. This approach uses a generator expression to iterate through each number in the array and sums the digits of each number using a nested loop. This allows the function to efficiently handle large arrays as it only processes each number once.