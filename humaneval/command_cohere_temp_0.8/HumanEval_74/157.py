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
    else:
        return []
```

The code calculates the total character count in the strings of both input lists and uses this to determine the return value. If the counts are equal, the first list is returned, and if the count of lst1 is less than that of lst2, lst1 is returned. If lst2 has a lower count, it's returned, and if both lists have zero-length, an empty list is returned. This logic ensures correct handling of the examples provided in the prompt.

Here's an example of using the function with a test case:
```python
test_cases = [
    ([], []),         # Empty lists
    ('[' 'hi' 'admin' ''], ['hI' 'Hi']),  # Exact match, return lst1
    ('[' 'hi' 'admin' ']', ['hi' 'hi' 'admin' 'project']),  # Contains lst2, return lst1
    ('[' 'hi' 'admin' ']', ['hI' 'hi' 'hi']),  # Contains lst1, return lst1
    ('[', '1' '2' '3' '4' '5']'),  # Return lst2
]

for t in test_cases:
    assert total_match(*t) == t[1]
```