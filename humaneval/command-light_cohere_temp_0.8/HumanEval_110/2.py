```python
def exchange(lst1, lst2):
    """
    Determine if it is possible to make lst1 contain only even numbers by performing
    an exchange of elements between lst1 and lst2.
    If returning true, if all elements of lst1 are even; otherwise, return false.
    """

def test_exchange():
    # Example 1: test the function
    [1, 2, 3, 4] = [1, 2, 3, 4]
    if exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES":
        assert True == True  # Passed
    else:
        assert False == True  # Failed

    # Example 2: try exchanging even and odd numbers
    [1, 2, 3, 4] = [1, 2, 3, 4]
    if exchange([1, 2, 3, 4], [1, 2, 3, -4]) == "YES":
        assert True == True  # Passed
    else:
        assert False == True  # Failed

    # Example 3: test passing lists of different lengths
    [1, 2, 3] = [1, 2, 3, 4]
    if exchange([1, 2, 3], [1]) == "YES":
        assert True == True  # Passed
    else:
        assert False == True  # Failed

    # Example 4: test passing empty lists
    [1, 2, 3] = []
    if exchange([1, 2, 3], []):
        assert True == False  # Passed
    else:
        assert False == False  # Failed

    # Example 5: test passing lists with different elements
    [1, 2, 'cat'] = [1, 2, 3]
    if exchange([1, 2, 'cat'], [1, 2, 3]) == "YES":
        assert True == True  # Passed
    else:
        assert False == True  # Failed

    # Example 6: test passing complex lists with odd and even numbers
    [1, 2, 3, 'cat'] = [1, 2, -3, 'cat']
    if exchange([1, 2, 3, 'cat'], [1, 2, -3, 'cat']) == "YES":
        assert True == True  # Passed
    else:
        assert False == True  # Failed
    ```