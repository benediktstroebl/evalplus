```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input array arr. For each element num, it converts it to an integer (using int(num)) and calculates the sum of its digits using a generator expression (sum(int(d) for d in str(num))). If the sum of digits is greater than 0, it contributes to the total count output. Finally, the function returns the total count of elements meeting the criteria.