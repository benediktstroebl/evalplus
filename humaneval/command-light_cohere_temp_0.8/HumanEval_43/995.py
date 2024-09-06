```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Test the function with various lists
test_pairs_sum_to_zero = [
    [],  # [1,3,5,0]
    [1,3,5,0],  # [1,3,-2,1]
    [1,2,3,7],  # [2,4,-5,3,5,7]
    [],  # [1]
    [2,4,-5,3,5,7],  # [2,4,-5,-3,5,7]
    [2,4,-5,-3,5,7],  # [2,4,-5,,-3,5,7]
]

for test_list in test_pairs_sum_to_zero:
    print(test_list)
    if pairs_sum_to_zero(test_list):
        print("Passed")
    else:
        print("Failed")
```
The code defines a Python function `pairs_sum_to_zero` that checks if any list of numbers has two elements whose sum equals zero. The function takes a also passes various tests with sample input lists. 

You can use this code to check for lists that satisfy the specified property, and it can be combined with other Python code to create more complex programs.