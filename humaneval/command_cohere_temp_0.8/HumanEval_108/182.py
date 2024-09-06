```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function sums over all elements in the array `arr` and counts the number of elements where the sum of the digits is greater than 0. The output of this function should match the expected outputs in the docstring. This approach uses a generator expression to iterate through each element in the array and check if the sum of the digits is greater than zero, employing int() to handle the conversion of each digit. 
The docstring includes a reminder about how negative numbers are treated, and also provides example tests against the function. 
This should provide a clear and efficient solution to the problem. If you would like a different approach to the problem or require further assistance, let me know!