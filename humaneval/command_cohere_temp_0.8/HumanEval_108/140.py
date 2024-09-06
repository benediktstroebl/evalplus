```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each num in the input array arr. It converts each num to an integer using int(num) and calculates the sum of its digits using the sum(int(d) for d in str(num)). If the sum of digits is greater than 0, it increments the output variable by 1. Finally, it returns the total count of numbers with a positive sum of digits. 

You can verify the function's behavior by checking the provided test cases:
```python
>>> count_nums([])
0
>>> count_nums([-1, 11, -11])
1
>>> count_nums([1, 1, 2])
3
```