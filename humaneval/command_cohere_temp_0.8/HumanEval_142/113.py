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
This function takes as input a list of integers, squares each element if its index is a multiple of 3, and cubes each element if its index is a multiple of 4 but not a multiple of 3. It then returns the sum of all elements. This approach uses the exponentiation operator (`**`) for its efficiency and brevity, avoiding the need for separate `square` and `cube` functions and reducing the number of iterations. The `enumerate` function allows us to access the index and value of each list element during the loop, which is then applied to the corresponding condition.  The function handles all cases as described in the prompt and efficiently computes the requested sum. 
The function can be tested as follows: 
```python
test_list = [1, 2, 3]
expected_result = 6

result = sum_squares(test_list)
print(f"For lst = {test_list}, the output is {result} (should be {expected_result})")
```
This will print: For lst = [1,2,3] the output is 6 (should be 6)

You can also test with empty list `[]` as follows:
```python
test_list = []
expected_result = 0

result = sum_squares(test_list)
print(f"For lst = {test_list}, the output is {result} (should be {expected_result})")
```
This will print: For lst = [] the output is 0 (should be 0)

Likewise, for a test list containing negative numbers:
```python
test_list = [-1, -5, 2, -1, -5]
expected_result = -126

result = sum_squares(test_list)
print(f"For lst = {test_list}, the output is {result} (should be {expected_result})")
```
This will print: For lst = [-1,-5,2,-1,-5] the output is -126 (should be -126)