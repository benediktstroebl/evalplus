```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test Case 1: Basic Function
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([2, 3, 4])
test_incr_list.append([5, 3, 4])
test_incr_list.append([5, 3, 4])
test_incr_list.append([5, 4])

def test_case1():
    assert incr_list(test_incr_list) == [2, 3, 4]

# Test Case 2: List with Tail Recursion
test_case2 = []
test_case2.append([5, 3, 5, 2, 3])
test_case2.append([1, 2, 3])

def test_case2_recursive():
    test_case2.append(test_case2_recursive())
    test_case2.append(test_case2)

def test_case2():
    assert test_case2_recursive() == [6, 5, 3, 4]

# Test Case 3: Custom List
test_case3 = [1, 2, 3]
test_case3.append(test_case3[1] + 1)
test_case3.append([2, 3, 4])

def test_case3():
    assert test_case3 == [2, 3, 5]

# Run All Tests
test_incr_list()
test_case1()
test_case2()
test_case3()
 ```
This script defines a function `incr_list` that adds one to the last element of a list and returns the updated list. It also includes three test cases to verify the correctness of the `incr_list` function. 
Please note that the actual output of the function will be displayed in your Python environment or IDE.