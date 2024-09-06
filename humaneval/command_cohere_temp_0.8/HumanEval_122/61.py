Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(int(d) for d in arr[:k] if len(str(d)) <= 2)
    return sum_two_digits
    # The above code can be rewritten as follows:
    # return sum(int(d) for d in arr[:k] if len(str(d)) <= 2)
```
This script provides the function `add_elements` that takes an array `arr` and an integer `k` as inputs and returns the sum of elements in `arr` that have at most two digits from the first `k` elements. This function uses a generator expression along with the `sum` function to calculate the sum of integers that fit the criteria.