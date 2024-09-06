```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function sums over all elements in the array `arr` and counts the number of elements where the sum of the digits is greater than 0. The output of this function should match the expected outputs given in the markdown code block.