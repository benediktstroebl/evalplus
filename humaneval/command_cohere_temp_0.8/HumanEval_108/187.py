```python
def count_nums(arr):
    return sum(sum(map(int, str(x))) > 0 for x in arr)
```

This solution uses a nested list comprehension that takes each element in the array and converts it to an integer, and then sums these integers. The test cases provided in the problem statement are covered by the provided function. You can test this function with additional int arrays to verify its functionality further. 

Let me know if this solution satisfies your requirements or if you'd like me to provide any additional help.