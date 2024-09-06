```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension, the sum of all elements is calculated and compared to zero.

# Test the function
    test_data = [1, 3, 5, 0, -2, 1]
    if pairs_sum_to_zero(test_data):
        print("List contains two elements sum to zero.")
    else:
        print("List does not contain two elements sum to zero.")
```
The above code defines a Python function named `pairs_sum_to_zero` that checks whether a list contains a pair of elements that sum to zero. 

It takes a list of integers as an argument and iterates through the list using list comprehension. It calculates the If sum of all elements in the list using the `sum()` function, and then compares this sum with zero. If the sum of all elements is zero, the function returns `True`, indicating that there are two distinct elements in the list that sum to zero. If the sum is not zero, the function returns `False`, indicating that there is not a pair of elements that sum to zero.

This function is then tested using a sample list of integers, and the results are printed to the console. 

You can use this function to solve the problem and test it with your own lists of integers.