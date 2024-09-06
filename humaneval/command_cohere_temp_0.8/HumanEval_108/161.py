```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(map(int, str(n))) > 0)
    return output
```
This function sums over all elements in the `arr` array, accumulating an integer result only for those elements whose summarized digits are greater than zero. This aligns with the problem statement's request to return the count of such elements.