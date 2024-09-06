```python
def total_match(lst1, lst2):
    char_count_lst1 = sum(len(str(item)) for item in lst1)
    char_count_lst2 = sum(len(str(item)) for item in lst2)
    if char_count_lst1 == char_count_lst2:
        return lst1
    elif char_count_lst1 < char_count_lst2:
        return lst1
    else:
        return lst2
```

The code uses two nested sum loops to calculate the total character count of strings in both lists. It then compares the counts to return the list with fewer characters, or the first list if both have the same count.

Here is an example usage of the function:
```python
print(total_match(['4'], ['1', '2', '3', '4', '5']))
```
```bash
['4']
```

And here is the markdown code block with corresponding test cases to verify the correct operation of the function:
```python
def test_total_match():
    # Case 1:
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # Added Test Cases:
    assert total_match(['aa', 'bb', 'cc'], ['aa', 'bb', 'dd', 'ee']) == ['aa', 'bb', 'dd', 'ee']
    assert total_match(['dog', 'cat', 'animal'], ['cat', 'dog', 'mouse', 'elephant']) == ['cat', 'dog', 'mouse', 'elephant']
    assert total_match(['1', '2', '3', '5'], ['1', '2', '3', '4', '5', '6', '7']) == ['1', '2', '3', '5']
    assert total_match(['a', 'b', 'c'], ['a', 'b', 'd', 'e', 'f']) == ['a', 'b', 'd', 'e', 'f']
```