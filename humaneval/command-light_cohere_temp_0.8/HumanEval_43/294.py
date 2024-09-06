```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    return any such  distinct set of elements sum up to zero.
```
 test_pairs_sum_to_zero = [
    [1, 3, 5, 0], 
    [1, 3, -2, 1], 
    [1, 2, 3, 7], 
    [2, 4, -5, 3, 5, 7], 
    [1]
]

for test in test_pairs_sum_to_zero:
    print(f"{test[0]} + {test[1]} = {test[2]}...")
    if not pairs_sum_to_zero(test):
        print("False")
    else:
        print("True")
```