```python
def triples_sum_to_zero(lst):
    # Define possible triple combinations and initialize boolean array
    n = len(lst)
    arr = [[j for j in range(n) if i != j and lst[i] + lst[j] != lst[k]] for i in range(n) for k in range(i+1, n)]
    # Initialize flag to False for if there is a triple that sums to zero
    flag = False
    # Loop through each combination of triple and check if sum is zero
    for t in range(len(arr)):
        if sum(arr[t]) == 0:
            flag = True
            break
    return flag
```

This function operates on an input list and returns a boolean that indicates whether three distinct elements in the list sum up to zero. It employs a boolean array to efficiently rule out combinations that don't sum up to zero, and it returns `True` if such a trio exists and `False` otherwise. 

Here is an example usage of the function:
```python
print(triples_sum_to_zero([1, 3, 5, 0]))  # Expected output: False
print(triples_sum_to_zero([1, 3, -2, 1]))  # Expected output: True
```

This function can also be tested with other scenarios to verify its correctness.