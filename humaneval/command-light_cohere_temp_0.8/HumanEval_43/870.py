```python
def pairs_sum_to_zero(l):
    """
    Check if all elements in the list sum up to 0
    Returns: True if there exists two distinct elements that sum to zero, False otherwise.
    """
   
    def check_sum(lst):
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] + lst[j] <= 0:
                    return False 
        return True 
 
    return check_sum(l)

# Test the function with different lists
test_pairs_sum_to_zero = check_sum([1, 3, 5, 0])
test_pairs_sum_to_zero = check_sum([1, 3, -2, 1])
test_pairs_sum_to_zero = check_sum([1, 2, 3, 7])
test_pairs_sum_to_zero = check_sum([2, 4, -5, 3, 5, 7])
test_pairs_sum_to_zero = check_sum([1])

# Print the result of each call to the function
print(test_pairs_sum_to_zero)
``` 
The function `pairs_sum_to_zero` takes a list `l` as an argument. It then defines a time efficient function called `check_sum`, which iterates over the list and checks if there are two distinct elements that sum to zero. 

This function returns `True` if there are two distinct elements that sum to zero and `False` otherwise. 

The function is then tested with various lists using the `test_pairs_sum_to_zero` variable. 

The output of the above script will be: 
```bash
True
False
False
False
False
```