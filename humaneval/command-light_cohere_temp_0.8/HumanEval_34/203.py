```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -VV, -INF, 0]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7, 8, 0],
    [-5, -3, -9, 0, "abc"],
    [-10, 0, -1]
]

for case in test_cases:
    print(unique(case))
``` 
This function uses the set data structure to keep track of elements seen so far, then uses a generator expression to only add elements to the output list if they are not in the set and not in the special negative values. 
This is a more efficient way to check for uniqueness compared to using a list comprehension with an if statement.