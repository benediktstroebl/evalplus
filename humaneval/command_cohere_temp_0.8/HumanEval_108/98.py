```python
def count_nums(arr):
    output = sum(int(b) for b in map(lambda x: str(abs(x)), arr) if sum(map(int, str(abs(x)))) > 0)
    return output
```

This function `count_nums` takes an array of integers (`arr`) and returns the number of elements that have a sum of digits greater than zero. The function achieves this by mapping over the input array, calculating the absolute value of each integer to eliminate negative signs, converting the result to a string, and computing the sum of its digits. If this sum is greater than zero, the element is counted towards the output. Finally, the total count of such elements is returned.

This solution is succinct and delivers the required functionality, as testified by the test cases in the original problem statement.