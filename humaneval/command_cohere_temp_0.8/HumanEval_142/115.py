```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
This Python script defines a function called sum_squares, which takes a list lst as input. It iterates through each element in the list using the enumerate function, which also gives the index of each element. Depending on whether the index is a multiple of 3 or 4, it squares or cubes the respective number. The squared or cubed values are accumulated in the result variable, which is then returned as the sum of all entries as specified in the problem statement. 

To ensure the code works correctly and conforms to the problem, the following tests can be run:
```python
test_sum_squares([1, 2, 3], 6)
test_sum_squares([], 0)
test_sum_squares([-1, -5, 2, -1, -5], -126)
```
These tests check edge cases and ensure that the function correctly squares and cubes the elements as stated in the problem. 
The implementation is efficient and has a time complexity of O(n), where n is the length of the input list.