Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```
```
Here is the solution of the function `count_nums`. It uses a conditional sum, iterating through each number in the array and counting the numbers whose digit sum is larger than 0.
```
The marker demonstrates that the provided solution follows the problem statement and test cases, ensuring the function `count_nums` correctly counts the number of elements in the array that have a sum of digits greater than 0. 
This solution has a time complexity of O(n), where n is the size of the input array.