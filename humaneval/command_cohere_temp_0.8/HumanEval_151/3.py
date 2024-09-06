```python
def double_the_difference(nums):
    odd_squares = [x**2 for x in nums if x % 2 == 1 and x >= 0]
    return sum(odd_squares) if odd_squares else 0
```

The function `double_the_difference` employs list comprehension to filter odd, non-negative integers from the input list (`nums`) and calculates the sum of their squares. The special case of an empty list is also addressed, returning 0. 

To validate the functionality of the script, three test cases are performed:
```python
test_list = [1, 3, 2, 0]
result = double_the_difference(test_list)
assert result == 10, "Failed test 1"

test_list = [-1, -2, 0]
result = double_the_difference(test_list)
assert result == 0, "Failed test 2"

test_list = [9, -2]
result = double_the_difference(test_list)
assert result == 81, "Failed test 3"

test_list = [0]
result = double_the_difference(test_list)
assert result == 0, "Failed test 4"

test_list = []
result = double_the_difference(test_list)
assert result == 0, "Failed test 5"
```

Each test is conducted to confirm the correctness of the function against the specified criteria. The tests cover scenarios including non-empty and empty lists, and lists containing various types of numbers. 

For the given problem, the proposed solution showcases an efficient and clear approach, which can be further enhanced by emphasizing the input validation aspect for real-world scenarios. This includes checking for types and providing meaningful error messages to ensure robustness.