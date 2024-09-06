Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(int(x) for x in arr[:k] if len(str(x)) <= 2)
    return sum_two_digits
```
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`. The function sums up the elements in `arr` that have at most 2 digits amongst the first `k` elements and returns the result.

To achieve this, it uses a list comprehension that iterates through the first `k` elements of `arr`, converting each element to an integer `x` and creating a generator expression with `len(str(x)) <= 2` to filter out elements that have at most 2 digits. The generator expression evaluates to a sum of the filtered elements using the `sum` function.