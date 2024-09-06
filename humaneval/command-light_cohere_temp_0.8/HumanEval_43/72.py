```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
Each integer is added to the variable sum, and the condition that the sum to zero is met is checked.
 # Example passing test:
    test_list = [1, 3, 5, 0]
    if pairs_sum_to_zero(test_list):
        print("List contains two distinct elements that sum to zero.")
    else:
        print("List does not contain two distinct elements that sum to zero.")
```
We are using the built-in function `sum()` to calculate the sum of the elements in the list. The function checks if the if the sum is equal to zero. It will return "True" if it meets the condition, and "False" otherwise. The test_list is a list of integers that is passed to the function as an argument. 

The test_list is the same list that was used in the first example. The same list is passed to the function in the same way as the original list of integers.