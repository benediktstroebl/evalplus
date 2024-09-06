Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(ele for ele in arr[:k] if len(str(ele)) <= 2)
    return sum_two_digits
```
This function `add_elements` takes an array `arr` and an integer `k` as inputs, and returns the sum of elements in the first `k` elements of `arr` that have at most two digits. It does so by using a generator expression within the sum function, which creates a iterable list of elements from the passed in array `arr` that have a length of at most 2 when converted into a string. Then it returns the sum of these values using the `sum` function. This solution should be efficient beyond the first 10 elements as it takes O(k) time for the sum to run, and then O(k) time for the generator expression, for a total of O(k^2) time. It should be optimized for larger inputs.