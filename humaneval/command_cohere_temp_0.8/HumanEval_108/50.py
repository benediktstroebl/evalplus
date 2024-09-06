```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
This function uses a generator expression that iterates through each element in the input list `arr`. It uses the `int` function to convert each element to an integer and checks if the integer is greater than or equal to zero using the `>= 0` condition. The `sum` function then adds up the number of elements that satisfy this condition, indicating the count of positive digit sum integers in the array.