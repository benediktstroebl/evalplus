```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each item in the input list `l` and compare each item to the threshold value `t`. 

You can test the function by calling it with different lists and threshold values. For instance, the below code tests the above function twice to confirm that it behaves as expected:
```python
# Tests:
print(below_threshold([1, 2, 4, 10], 100)) # Should print True
print(below_threshold([1, 20, 4, 10], 5)) # Should print False
```
The function should return `True` when used with the first example test case, and `False` when used with the second example test case. 

Please let me know if you would like me to explain any part of this solution in more detail!