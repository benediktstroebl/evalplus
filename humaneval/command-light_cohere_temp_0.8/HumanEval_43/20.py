```python
def pairs_sum_to_zero(l):
    """
    Check if all the elements in the list sum to zero.
    Return True if two ares sum to zero and the list has at least two distinct elements,
    and False otherwise.
    """
    list comprehension and the sum of the elements in the list must be zero:
    return all([x == 0 for x in l])

test_pairsum_to_zero = []
test_pairsum_to_zero.append([1, 3, 0])
test_pairsum_to_zero.append([1, 3, 1])
test_pairsum_to_zero.append([1, 3, -1])
test_pairsum_to_zero.append([1, -2, 3])
test_pairsum_to_zero.append([1, 2, 3])

def sum_to_zero(test_list):
    """
    Use the function pairs_sum_to_zero to check if the list can be divided into two lists that sum to zero
    """
    return pairs_sum_to_zero(test_list)

# Run the function sum_to_zero and print the results
test_pairsum_to_zero([1, 3, -2, 1])
print("Result:", sum_to_zero([1, 3, -2, 1])  == True)
test_pairsum_to_zero([1, 2, 3, 7])
print("Result:", sum_to_zero([1, 2, 3, 7]) == False)
test_pairsum_to_zero([2, 4, -5, 3, 5, 7])
print("Result:", sum_to_zero([2, 4, -5, 3, 5, 7]) == True)
test_pairsum_to_zero([1])
print("Result:", sum_to_zero([1]) == False")
```
This Python script defines a function `sum_to_zero` that checks whether a given list can be divided into two lists with sums to zero. The function uses the `pairs_sum_to_zero` to perform the check and returns `True` if the list can be divided into two lists with sums to zero and `False` otherwise. The `pairs_sum_to_zero` function checks if all the elements in the list sum to zero. This script also includes a tests that verify the correctness of the `sum_to_zero` function using a test suite. 
The test suite contains a list of test cases, which are lists of integers. The `sum_to_zero` function is then called with each test case, and the result is printed.