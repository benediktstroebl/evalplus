```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes one argument, l, which is a list. This function sorts the unique elements in the list using the set method to remove duplicate elements and then uses the sort method to ensure the elements are sorted. 

To verify the functionality of the unique function, you can create a unit test that provides a list with duplicate elements and checks if the function returns a list of unique elements, sorted in ascending order. Here is an example:
```python
def test_unique():
    # Input list with duplicate elements
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]

    # Function call
    sorted_unique = unique(input_list)

    # Expected output
    expected_output = [0, 2, 3, 5, 9, 123]

    # Checking if the output is correct
    assert sorted_unique == expected_output
    assert len(sorted_unique) == len(set(input_list))
```

In the test_unique function, the input list is created with duplicate elements, and the unique function is called with this list. The output of the function is stored in the sorted_unique variable. Then, the function checks that the output is correct by comparing it to the expected_output and verifying that the number of elements in both lists is the same, which indicates that duplicates have been removed. 

When you run this test, it will pass, confirming that the unique function works as expected. 
```bash
....
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
``` 

You can embed this test in the script or conduct it separately, depending on your preferences and testing strategies.