```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test case 1
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

#Test case 2
def test_get_positive2():
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

#Main code
if __name__ == "__main__":
    test_get_positive()
    test_get_positive2()
```
The function get_positive takes a list l as input and returns a new list containing only the positive numbers from l. The function uses list comprehension with the condition num >= 0 to filter out the negative numbers from l. 

The test cases, test_get_positive and test_get_positive2, pass assert statements to verify that the output of the get_positive function is correct for a given list. 
Finally, the main code block runs the test cases and checks if the function is working as expected.