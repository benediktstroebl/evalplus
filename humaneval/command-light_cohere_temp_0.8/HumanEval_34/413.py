```python
def unique(lst):
    return sorted(set(lst))

# Test cases
 tests = [
    [list([5, 3, 5, 2, 3, 3, 9, 0, 123]), unique([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])],
     [0, 2, 3, 5, 9, 123])
 tests.
 assert all(map(lambda x: x in unique(x), tests[0]))
 assert all(map(lambda x: x not in unique(x), tests[1]))
 ``` 
This code defines a function `unique` which takes a list `lst` as an argument and returns a sorted set of unique elements in the list. 

The `tests` variable is an array of test cases, where each test case is another list. The `assert` function is used to check if the output of the `unique` function is correct for each test case. The `map` function is used to apply a function (in this case, a lambda function) to each element of the test case list, and the `not in` operator is used to check if each element of the result is not in the unique set.