```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function sums over all elements in the array `arr` and counts the number of elements where the sum of the digits is greater than 0. It does so by first converting the elements to integers using `int(n)`. Then, it computes the sum of the digits by converting the integer to a string using `str(n)` and extracting the digits using a generator expression `int(d) for d in str(n)` where `d` iterates over each digit. Finally, it sums these digits and checks whether the result is greater than 0.