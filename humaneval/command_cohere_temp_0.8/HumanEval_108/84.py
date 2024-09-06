```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each num in the input array arr. It converts each num to an integer using int(num) and calculates the sum of its digits using the sum(int(d) for d in str(num)). If the sum of the digits is greater than 0, it contributes to the count. Finally, it returns the total count of numbers with positive digit sums.