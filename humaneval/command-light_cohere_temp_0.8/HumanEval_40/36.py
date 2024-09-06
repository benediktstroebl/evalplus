Here's the code to solve the problem:

```python
def is_sum_to_zero(lst):
    sum = 0
    for i in lst:
        if sum + i > 0:
            sum += i
    return sum <= 0
```

This code defines a function `is_sum_to_zero` that takes a list of integers as an input. It iterates over each list, and if it finds an element that when added to the running sum is greater than 0, it adds that element to the sum. The function returns True if the sum is less than or equal to 0, and False otherwise.