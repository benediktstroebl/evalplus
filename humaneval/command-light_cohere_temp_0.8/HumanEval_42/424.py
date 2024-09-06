```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [0] * (n + 1)
    for i in range(n):
        result[i+1] = l[i] + 1
    return result

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result1 = incr_list(test_case1)
assert list(test_result1) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 2
test_case2 = [1, 2, 3, 4]
test_result2 = incr_list(test_case2)
assert list(test_result2) == [2, 3, 4, 5]

# Test case 3
test_case3 = [5, 2, 3, 4, 3, 3]
test_result3 = incr_list(test_case3)
assert list(test_result3) == [6, 4, 6, 3, 4, 4]
```
This Python code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. It then tests three simple cases to test the correctness of this function:
1. After defining the incr_list function, it creates test_case1, which is a list with values [5, 3, 5, 2, 3, 3, 9, 0, 123]. It then calls the incr_list function with this list and stores the result in test_result1.
2. The code then asserts that test_result1 is equal to [6, 4, 6, 3, 4, 4, 10, 1, 124] using the assert statement. It checks if the same element matches the expected result.
3. The code then creates test_case2, which is a list with values [1, 2, 3, 4]. It then calls the incr_list function with this list and stores the result in test_result2.
4. The code asserts that test_result2 is equal to [2, 3, 4, 5] using the assert statement.
5. Finally, the code creates test_case3, which is a list with values [5, 2, 3, 4, 3, 3]. It then calls the incr_list function with this list and stores the result in test_result3.
6. The code then performs the final assertion, which checks if test_result3 is equal to [6, 4, 6, 3, 4, 4]. If all assertions pass, it means that the incr_list function is working correctly.