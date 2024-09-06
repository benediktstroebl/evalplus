```python
def total_match(lst1, lst2):
    char_count_lst1 = sum(len(x) for x in lst1)
    char_count_lst2 = sum(len(x) for x in lst2)
    if char_count_lst1 == char_count_lst2:
        return lst1
    elif char_count_lst1 < char_count_lst2:
        return lst1
    elif char_count_lst1 > char_count_lst2:
        return lst2
    return []
```

The code calculates the total character count in the strings of both lists, `lst1` and `lst2`. If both lists have the same count, the function returns the first list (`lst1`). If one list has fewer characters than the other, the function returns the list with the fewer characters, otherwise, it returns an empty list.  This algorithm follows the guidelines mentioned in the problem statement.

The unit tests correspond to the examples provided in the problem statement:
```python
test_total_match = unittest.TestCase()

test_total_match.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])
test_total_match.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])
test_total_match.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])
test_total_match.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])
test_total_match.assertEqual(total_match([], []), [])
test_total_match.assertEqual(total_match(['aa', 'b'], ['a', 'aa', 'c', 'd']), ['aa', 'b'])
```