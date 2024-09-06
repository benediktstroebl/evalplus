```python
def incr_list(lst):
    return [i + 1 for i in lst]

def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This Python code defines a function incr_list that adds 1 to each element of a list, and a test function test_incr_list that checks the correctness of the incr_list function using test cases.  It test of using descriptive variable names and follows PEP 8 naming conventions, which enhances code readability.