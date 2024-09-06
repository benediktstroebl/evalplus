Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(int(x) for x in arr[:k] if len(str(x)) <= 2)
    return sum_two_digits
```
This function takes an array `arr` and an integer `k` as inputs, and returns the sum of elements in `arr` that have at most two digits from the first `k` elements. It does this by using a generator expression and the `sum` function to sum up the integers that have lengths less than or equal to 2. The markdown code block is also included for better readability.