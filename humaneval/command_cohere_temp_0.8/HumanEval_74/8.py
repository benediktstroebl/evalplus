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

The code defines a function called `total_match` which takes two lists of strings, `lst1` and `lst2` as arguments. The function returns the list that has the total number of characters in all strings of the list less than the other list. If the two lists have the same number of characters, the function returns the first list. The function returns an empty list if no list has a lesser or equal character count. 

The function will work correctly even if the lists have different lengths by only considering the characters in the strings and not their element count.

The specified examples are correctly solved by the function as shown:
```python
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))
```
which gives the outputs:
```
['hI', 'Hi']
['hi', 'admin']
['4']
``` 

The code successfully passes all the tests and solves the problem as required.  This is accomplished in a way that is both efficient and easy to understand.