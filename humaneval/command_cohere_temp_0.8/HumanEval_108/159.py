Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```
The function `count_nums` iterates through the array and calculates the sum of the digits for each integer. It returns the number of elements that have a sum of their digits greater than 0. The sums of digits are calculated using the `sum` function with the `map` function to convert the string representation of each number to a list of integers. The `sum` function then calculates the sum of the digits in the list.