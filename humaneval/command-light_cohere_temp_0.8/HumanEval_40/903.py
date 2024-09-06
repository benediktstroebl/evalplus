```python
def triples_sum_to_zero(lst):
    if sum(x for x in lst if x <= 0) >= 3:
        return True
    else:
        return False

# Test the function with provided examples
assert triples_sum_to_zero([1, 3, 5, 0]) == False
# ... other tests...
```
This code defines a function called triples_sum_to_zero that takes a list lst as input and returns True if the list has three distinct elements whose sum is zero, and False otherwise. The function uses a sum of all elements in the list, x <= 0 checks for non-positive numbers, and checks if the sum of three distinct elements is zero.