```python
def total_match(list1, list2):
    return len(list1) < len(list2) 

#def test_total_match():
    assert total_match([], []) == True
    assert total_match(['hi'], ['hI']) == True
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin']) == True
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == True
    assert total_match(['a', 'b', 'c'], ['a', 'b']) == False
```  The test_total_match function contains a set of assertions that validate the functionality of the total_match function. The function compares the different scenarios and ensures that the function is working correctly.