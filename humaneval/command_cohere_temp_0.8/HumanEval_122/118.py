Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(ele for ele in arr[:k] if len(str(ele)) <= 2)
    return sum_two_digits
    # The line above uses a generator expression to create a sequence of integers from the first k elements of arr, and then sums them if their string representation has at most two digits (which corresponds to integers with values less than or equal to 99).
```

This script has a function `add_elements(arr, k)` that takes two inputs, a list `arr` and an integer `k`. The function returns the sum of the elements that have at most two digits from the first `k` elements of `arr`. This is done using a generator expression `sum(ele for ele in arr[:k] if len(str(ele)) <= 2)` which creates a sequence of integers from the first `k` elements of `arr` and then sums them if their string representation has at most two digits. This condition effectively filters out any integers with more than two digits, considering only those that have values less than or equal to 99.

The script adheres to the problem statement's constraints, guaranteeing that it operates correctly so long as the input array `arr` has at most 100 elements and the number `k` is between 1 and the length of `arr`.