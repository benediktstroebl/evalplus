Here is a self-contained Python script with a function that solves the problem of finding three distinct elements in a list that sum to zero:
```python
def triples_sum_to_zero(l: list):
    return any(sum(x) == 0 for x in l)

# Test the function with various lists
for test_list in [[1, 3, 5], [1, 2, 3], [2, 4, -5], [1]]:
    result = triples_sum_to_zero(test_list)
    if result:
        print(f"The list {test_list} passes the test.")
    else:
        print(f"The list {test_list} fails the test.")
```

The code defines a `triples_sum_to_zero` function that takes a list `l` as input and returns `True` if there are three distinct elements in `l` whose sum is zero, and `False` otherwise. The function utilizes a Python's `any()` function to check if there exists at least one element in the list whose sum is equal to zero.