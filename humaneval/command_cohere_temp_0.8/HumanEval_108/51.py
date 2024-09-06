```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input list `arr`. It converts each element `n` to an integer using `int(n)` and calculates the sum of its digits using a nested generator expression in `sum(int(d) for d in str(n))`. Then, it checks if this sum is greater than zero and includes the element in the count if it is. Finally, it returns the total count of elements meeting this condition.