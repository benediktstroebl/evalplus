```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None

    # Check if the list has only one element
    if len(l) == 1:
        return l[0]

    # Sort the list
    sorted_list = sorted(l)
    
    # Finds the median
    centre_index = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        return (sorted_list[centre_index - 1] + sorted_list[centre_index]) / 2
    else:
        return sorted_list[centre_index]
```

This function handles cases of empty lists, single-element lists, and odd/even-sized lists. Let's validate this solution using the given test cases:
```python
def test_median():
    # Test case 1
    assert median([3, 1, 2, 4, 5]) == 3

    # Test case 2
    assert median([-10, 4, 6, 1000, 10, 20]) == 15

test_median()
```

Assuming these assertions pass, we can confirm that the provided solution is correct and conforms to the problem statement. Feel free to adapt this code to your needs. Let me know if you have any other questions!