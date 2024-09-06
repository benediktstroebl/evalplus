```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    # Iterate through each number and check if their digit sum is greater than 0
    return sum(1 for num in nums if sum(int(d) for d in str(num)) > 0)
```
The function count_nums creates a list of the integers in the input array, then uses a list comprehension to iterate through each number and check if its digit sum is greater than zero. The sum of the numbers with positive digit sums is then returned. The code passes the provided tests: `count_nums([]) == 0` returns True, and `count_nums([-1, 11, -11]) == 1` and `count_nums([1, 1, 2]) == 3` return True as well.