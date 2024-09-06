```python
def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        strings = [word for word in lst if len(word) % 2 == 0]
        strings.sort(key=len, reverse=True)
        strings.sort()
        return strings
```

The function first checks if the length of the list is even to return the list as it is. Otherwise, the function filters out the strings that have odd lengths and sorts them first by length in a descending order and then alphabetically. The function returns the sorted list of strings.

#### Here is a test suite that can be used to test the above function:
```python
import pytest

def test_correct_list_return():
    test_list = ["aa", "a", "aaa", "ab", "c", "aaa", "cd"]
    expected_output = ["aa", "aaa", "aaa", "ab", "c", "cd"]
    assert sorted_list_sum(test_list) == expected_output

def test_empty_list_return():
    test_list = []
    assert sorted_list_sum(test_list) == []

def test_single_word_list_return():
    test_list = ["bb"]
    assert sorted_list_sum(test_list) == ["bb"]

def test_list_with_odd_words_return():
    test_list = ["aa", "a", "aaa", "ab", "c", "aaa", "cd", "odd"]
    expected_output = ["aa", "a", "aaa", "aaa", "ab", "c", "cd"]
    assert sorted_list_sum(test_list) == expected_output
```