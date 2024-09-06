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
The function sums over the list, updating each element value according to its index rules, and returns the summed value. 

You can verify the functionality with the following test cases:
```python
test_cases = [[1, 2, 3], [], [-1, -5, 2, -1, -5]]
expected_results = [6, 0, -126]

for test, result in zip(test_cases, expected_results):
    assert sum_squares(test) == result
``` 

The code passes each test case above with the expected results: [6, 0, -126]. 
Would you like to know more about the code or any specific problem within it? Feel free to ask for more detail on any of the problems presented here.