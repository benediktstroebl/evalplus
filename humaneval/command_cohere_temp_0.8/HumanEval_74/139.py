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
The code uses two variables to calculate the total character count of the strings in each list. It then simply returns the list with the lower character count. If the counts are the same, it returns the first list. The method is straightforward and intuitive, which should make it reasonably scalable to large inputs. 
The unit tests are included to ensure the function works correctly:
```python
test_cases = {
    'empty': ([], []),
    'identical': ('hi', 'hi'),
    'different case': ('hI', 'Hi'),
    'shared substrings': ('hi', 'hi', 'admin', 'project'),
    'additional strings': ('hI', 'hi', 'hi'),
    'reverse': ('4', '1', '2', '3', '4', '5')
}
for key, value in test_cases.items():
    assert total_match(*value) == expected_result
```