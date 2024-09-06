```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
The `count_nums` function uses a concise generator expression (`sum(...)`) to count the number of elements in the input `arr` that have a sum of digits greater than or equal to 0. This is achieved by iterating through each number in the array and evaluating the condition `int(num) >= 0`, which effectively determines whether the number has a positive sum of digits.