```python
def total_match(lst1, lst2):
    l1, l2 = len(lst1[0]), len(lst2[0])
    for i in range(min(len(lst1), len(lst2))):
        if l1 + l2 == sum(len(x) for x in lst2):
            return lst1
        if l2 + l1 == sum(len(x) for x in lst1):
            return lst2
    return lst1 if l1 <= l2 else lst2
```

The solution employs the `sum()` function to compute the total character count of both lists' strings. By doing so, it determines whether the count is less in the second list (`lst2`) or first list (`lst1`). If the total character count is less in `lst2`, it provides a list of strings from `lst1` and `lst2` whereby the total character count matches `lst1 + lst2`. If the total character count is less in `lst1`, it provides a list of strings from `lst1` and `lst2` whereby the total character count matches `lst2 + lst1`. If the lengths of both lists are less, then it returns the first list `lst1` as the character count of `lst1` is always less than the character count of `lst2` owing to the increasing nature of the character count sum.

Here is a markdown code block incorporating test cases to validate the correctness of the script:
```python
def test_total_match():
    # Basic tests:
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # Edge case where the smaller list has a single string:
    assert total_match(['abcd'], ['a', 'b', 'c', 'd', 'e']) == ['abcd']
    assert total_match(['abcd'], ['ab', 'bc', 'cd', 'd']) == ['abcd']

    # Edge case where the smaller list has multiple strings:
    assert total_match(['ab', 'cd'], ['a', 'b', 'c', 'd', 'e']) == ['ab', 'cd']
    assert total_match(['ab', 'cd'], ['ab', 'bc', 'cd', 'd']) == ['ab', 'cd']

    # Longer list has a single string:
    assert total_match(['abcde'], ['a', 'b', 'c', 'd', 'e', 'f']) == ['abcde']
    assert total_match(['abcde'], ['ab', 'bc', 'cd', 'de', 'e']) == ['abcde']

    # When the character counts are equal:
    assert total_match(['a', 'b', 'c'], ['a', 'b', 'c', 'd']) == ['a', 'b', 'c']
    assert total_match(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd', 'e']) == ['a', 'b', 'c', 'd