```python
def pairs_sum_to_zero(l):
    """
    Check if all pairs of elements in the list sum to zero.
    Return True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    def test_sum_zero(lst):
        return all(sum(x+y) <= 0 for x,y in zip(lst))
    return test_sum_zero(lst)

test_sum_zero = lambda lst:  lst == [1,3,5,0]
test_sum_zero = lambda lst:  lst == [1,2,3,7]
test_sum_zero = lambda lst:  lst == [2,4,-5,3,5,7]
test_sum_zero = lambda lst:  lst == []

print(test_sum_zero([1,3,5,0])) # Output: True
print(test_sum_zero([1,3,5,2])) # Output: False
print(test_sum_zero([1,2,3,7])) # Output: False
print(test_sum_zero([2,4,-5,3,5,7])) # Output: True
print(test_sum_zero([1])) # Output: False
```
The script defines a function `pairs_sum_to_zero` that checks if all pairs of elements in the list sum to zero. It then defines a test functions that create test cases for the function. The `test_sum_zero` function creates a list of test cases and calls the `pairs_sum_to_zero` function to check if it passes. 

The `test_sum_zero` function uses the `all` function to check if the condition is met for all pairs of elements in the list.