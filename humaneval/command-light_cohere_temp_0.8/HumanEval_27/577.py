```python
def flip_case(string):
    return ''.join_case(string)

def _test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'dlROW'
    assert flip_case('123') == '123'
    assert flip_case('tomorrow') == 'tomOrNdRow'

# Call the function with test harness
test_flip_case()
```
This Python script defines a function `flip_case` that converts a given string to a case-flipped version. The script also includes a `test_flip_case` function, which provides test cases to validate the `flip_case` function. 

Finally, the `test_flip_case()` function is called to run the test harness.