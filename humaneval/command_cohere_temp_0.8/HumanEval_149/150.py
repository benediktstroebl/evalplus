```python
def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort function sorts strings in lexicographic order
    return sorted(lst_result)
```

The method eliminates strings with an odd length from the list and returns the remaining elements in sorted order. The sort is performed in lexicographic order, which organizes the list alphabetically.

This algorithm efficiently tackles the problem at hand and showcases the usage of a concise and optimized approach. 

If you would like to test this script, you can create a file called `test_sorted_list_sum.py` and add the following code:
```python
import unittest

def test_sorted_list_sum():
    # Test case 1
    lst = ['aa', 'a', 'aaa', 'ab', 'c', 'aaa', 'bc']
    expected = ['aa', 'a', 'aaa', 'ab', 'c', 'aaa', 'bc']
    result = sorted_list_sum(lst)
    assert result == expected

    # Test case 2
    lst = ['ab', 'a', 'aaa', 'cd', 'c', 'aaa', 'de']
    expected = ['ab', 'cd', 'a', 'aaa', 'c', 'aaa', 'de']
    result = sorted_list_sum(lst)
    assert result == expected

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with two test cases that cover different scenarios. You can use `unittest` to run the tests and verify that the function behaves as expected.