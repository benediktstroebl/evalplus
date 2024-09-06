Here is a Python script with a self-contained function that solves the problem of finding two sum-to-zero elements in a list:
```python
def pairs_sum_to_zero(l):
    return sum((x+y) <= 0 for x, y in zip(l, l[1:])) == len(l)
```
The function is designed to determine whether a list of integers contains any pair that adds up to zero. This is done through using a 'zip' function to simultaneously iterate over the elements of the list and its reverse. 

This method has a time complexity of O(n^2) due to the nested iteration, but it provides a straightforward and self-contained solution for the problem.