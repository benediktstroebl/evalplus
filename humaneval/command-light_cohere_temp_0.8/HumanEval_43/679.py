```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Test the function with some examples
for test_case in [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [2, 4, -5, 3, 5, 7],
    [1]
]:
    result = pairs_sum_to_zero(test_case)
    if result:
        print(f"List has two distinct elements sum to zero: {test_case}")
    else:
        print(f"List does not have two distinct elements sum to zero: {test_case}")

``` 
This Python function determines whether a list contains any pairs whose sum equals zero. It employs the colleague list comprehension and the ever-useful zip() method. The function returns True if there are two distinct elements in the list that sum to zero, and False otherwise.