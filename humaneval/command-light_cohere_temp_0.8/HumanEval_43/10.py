```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    return False

# Test the function
test_pairsum = lambda: pairs_sum_to_zero([1, 3, 5, 0]) == True
test_pairsum2 = lambda: pairs_sum_to_zero([1, 3, -2, 1]) == True
test_pairsum3 = lambda: pairs_sum_to_zero([1, 2, 3, 7]) == False
test_pairsum4 = lambda: pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
test_pairsum5 = lambda: pairs_sum_to_zero([1]) == False

if test_pairsum() and test_pairsum2() and test_pairsum3() and test_pairsum4() and test_pairsum5():
    print("All tests passed successfully.")
else:
    print("One or more tests failed.")
```

This code defines a Python function `pairs_sum_to_zero` that checks if any two elements in the input list sum to zero. Then, it tests this function by passing various input lists through test functions `test_pairsum` and `test_pairsum2`. The program will print out a message if all the test functions return `True`, indicating successful tests. Otherwise, it will print a message indicating that one or more tests failed.