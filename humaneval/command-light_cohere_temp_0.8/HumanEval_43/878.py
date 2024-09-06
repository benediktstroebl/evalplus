```python
def pairs_sum_to_zero(l):
    """
    Function that returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    take a dry run list comprehension and a simple sum test
    """
    return any([x+y!=0 for x,y in zip(l, l[1:])])

# Test
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for i, test in enumerate(test_cases):
    result = pairs_sum_to_zero(test)
    print(f"{test} -> {result}").format(test))
    if result != test[0]:
        print("Error:", result, test != expected)
```