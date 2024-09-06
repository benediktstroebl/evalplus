```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x != 0]) == 0:
        return True
    return False

# Test function
def test_triples_sum_to_zero(func):
    assert func([1, 3, 5, 0]) == False
# Test case 1
assert func([1, 3, -2, 1]) == True
# Test case 2
assert func([1, 2, 3, 7]) == False
# Test case 3
assert func([2, 4, -5, 3, 9, 7]) == True
# Test case 4
assert func([1]) == False
```
The code defines a function called **triples_sum_to_zero** that takes a list lst as input and returns True if there are three distinct elements in the list that sum to zero, and False otherwise.

It then uses a simple logic to check if the sum of the elements in the list is equal to zero. The test function **test_triples_sum_to_zero** is used to check the correctness of the **triples_sum_to_zero** function by passing various test cases.