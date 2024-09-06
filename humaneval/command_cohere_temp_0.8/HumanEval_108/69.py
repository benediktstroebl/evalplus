```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input list and determine if the sum of its digits is greater than 0. The overall sum is then counted and returned as the final result. 

Here is the solution corresponding to the test cases provided:
```python
def test_count_nums():
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3
    assert count_nums([1, 2, 3, 4, 5]) == 5
    assert count_nums([-3, -2, -1, 1, 2]) == 3
    assert count_nums([0, 0, 0, 0, 0]) == 1
test_count_nums()
```
This code provides additional test cases to ensure that the `count_nums` function works correctly and meets the problem requirements. The final line executes the test_count_num() function to verify the functionality of the `count_nums` function.  This will run the function and check if the expected output matches the output of the function for the given input. 
The solution maximizes the use of built-in Python functionalities such as summing generators with `sum`, and using `str` to digitize integers and `int` for conversions, making the code concise and efficient.  This showcases Python's expressiveness and simplicity in solving discrete mathematics problems.