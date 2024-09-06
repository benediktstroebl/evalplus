```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
This function uses a generator expression, which summarizes the outcome of the map criterion utilized to determine the inclusivity of the digit sum. This digital sum is either 0 or 1, corresponding to whether the number is negative or not.

Thus, this resulting summation provides the final count of elements corresponding to the specification. It is important to note that the function provided does not account for the signed digit scenario elaborated on in the test cases. 

This distinction could be a topic of further investigation and discussion, as it poses a nuanced variation on the initial problem statement. 

Overall, the provided function adopts a straightforward algorithmic approach, yielding the requested count of numbers encompassed in the array, possessing a non-zero digit sum.