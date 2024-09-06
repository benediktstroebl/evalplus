```python
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in x]
    return [n for n in x if bool(odd_digits)] + [n for n in odd_digits]
``` 

The function employs two nested lists comprehensions to filter out numbers with odd digits (resulting in `odd_digits`), and then checks which numbers in the input list have corresponding odd digits in this list. Lastly, it also includes the numbers from `odd_digits` if they weren't already present in the input list. The tests for the function can be run using the following code:
```python
def test_unique_digits():
    # Test case 1
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # Test case 2
    assert not unique_digits([152, 323, 1422, 10]) 
    
    # More test cases can be added as needed
    ``` 
This should give you a good starting point to understand the code and to test its functionality locally in your Python environment. Let me know if you have any questions.