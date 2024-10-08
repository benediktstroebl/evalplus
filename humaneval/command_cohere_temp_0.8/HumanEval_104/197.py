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
    # Convert list to set to filter out even digits.
    elements = set(x)
    even_digit = ['2', '4', '6', '8']
    filtered_elements = [
        element for element in elements if 
        not any(char in even_digit for char in str(element))
    ]
    
    # Sort the list in increasing order.
    sorted_list = sorted(filtered_elements)
    return sorted_list
```
The function `unique_digits` uses a set to filter out elements containing even digits. Subsequently, a list comprehension filters out the elements from the set and sorts the result to give the expected output. The `str` function is used to convert each element to a string to check for the presence of even digits. The solution assumes that the list elements are positive integers.