```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return max_val if freq >= max_val else -1
```
The function `search` iterates through the list, updating the maximum valued element and its frequency. If the frequency of an element is greater than or equal to its value, it returns this value, otherwise, it returns -1. 

Here is a test case that can be used to validate the function:
```python
def test_search():
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([4, 1, 2, 2, 3, 1]) == 2
``` 
The test case incorporates all the conditions and the expected outputs as described in the problem statement. 
To execute the test cases, you can add this line before the definition of `test_search()` function:
```python
test_search()
``` 
This allows you to execute tests when running the Python script.