```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function sums over all elements in the `arr` array if the digit-wise sum of each element is greater than 0. The digit-wise sum of the number is negative for a negative number, so we need to exclude such cases. The function returns the counted number of elements with a sum of digits greater than 0. The resulting outcome is 1 for inputs like `[1, 1, 2]`, and 3 for `[1, 11, -11]`.