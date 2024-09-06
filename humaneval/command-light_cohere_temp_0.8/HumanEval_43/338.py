```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
# List of test cases
t = [
    [1, 3, 5, 0], 
    [1, 3, -2, 1], 
    [1, 2, 3, 7], 
    [2, 4, -5, 3, 5, 7], 
    [1]
]

for test in t:
    result = pairs_sum_to_zero(test)
    if result == False:
        print("Test", test, "failed")
    else:
        print("Test", test, "passed")
```