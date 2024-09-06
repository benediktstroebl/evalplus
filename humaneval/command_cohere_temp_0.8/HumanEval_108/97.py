```python
def count_nums(arr):
    output = sum(int(num) >= 0 for num in arr)
    return output
```
This function uses a generator expression to iterate through each number in the array and determines whether its digits' sum is greater than zero by converting it to an integer and checking if it's greater than or equal to zero. It then returns the total count of such numbers.