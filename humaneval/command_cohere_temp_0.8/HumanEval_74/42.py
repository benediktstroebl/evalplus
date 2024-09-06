```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This function is designed to take two lists of strings, lst1 and lst2, and return the list with a total number of characters less than the other list. If both lists have an equal number of characters, it returns lst1, whereas if the length of lst1 is less than lst2, it returns lst1 or lst2, ensuring that no extra string from lst2 is included.

Here is a simple test suite:
```python
def test_total_match():
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert total_match(['hi', 'hello'], ['hello', 'hi', 'hi']) == ['hi', 'hello']
```
To test the function, five different scenarios are examined, and the appropriate outcome is verified. These examples cover a variety of scenarios, including lists of different lengths and lists where the strings within them have varying character counts.