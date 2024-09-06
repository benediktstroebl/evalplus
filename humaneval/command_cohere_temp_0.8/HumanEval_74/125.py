```python
def total_match(lst1, lst2):
    l1, l2 = len(lst1[0]), len(lst2[0])
    for i in range(min(len(lst1), len(lst2))):
        if l1 + l2 == sum(len(x) for x in lst2):
            return lst1
        elif l1 + l2 > sum(len(x) for x in lst2):
            return lst2
        l1 += len(lst1[i])
        l2 += len(lst2[i])
    return lst1 if l1 <= l2 else lst2
```

The algorithm for the function `total_match()` is based on the following:
1. To solve the problem, we assume that we have two lists of strings, `lst1` and `lst2`, the problem asks to return the list with the total number of characters in all strings less than the other list.
2. The total number of characters in a list can be computed by the sum of the length of each string in the list. So we compute these sums for `lst1` and `lst2` at the beginning of the algorithm in the lines `l1, l2 = len(lst1[0]), len(lst2[0])`. 
3. The algorithm then loops through both lists, and at each step, we add the length of the current string in each list to the total char count `l1` and `l2`. 
4. We also check the current total against the total char count of `lst2`. If the current total of `l1` + `l2` is equal to the total char count of `lst2`, we return `lst1` as requested. We also swap `lst1` and `lst2` as requested in the problem statement.
5. If the total of `l1` + `l2` is greater than the total char count of `lst2`, we break the loop and return `lst2` as requested. 
6. Finally, after the loop, we check if the total of `l1` is less than or equal to `l2`, if so, it means the total char count of `lst1` is less than the total char count of `lst2`, so we return `lst1`. 

The function assumes that both lists contain at least one string, if not, it would raise an error. It also assumes that strings have positive lengths, if not, the total character count would not be accurate. 

We can test this function using the following test cases:
```python
def test_total_match():
    # basic tests
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # edge case
    assert total_match(['1', '2', '3', '4', '5'], ['5']) == ['5']

    # case when total chars are the same but one list has more items
    assert total_match(['1', '2', '3', '4', '5'],