```python
def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    # sort by length and alphabetically
    lst_new.sort(key=lambda x: (len(x), x))
    return lst_new
```

The function `sorted_list_sum` uses a list comprehension to filter out strings with odd lengths from the input list `lst`.

After filtering, the function sorts the new list by the length of each string using the `sort` method and a lambda function as the sorting key. If two strings have the same length, the alphabetic order is used as the secondary sorting criterion. 

The expected output is returned sorted by the length of each word, and if two words have the same length, the result is also sorted alphabetically.

This code should pass the given tests. You can incorporate the given tests into the code to ensure that the function behaviour is correctly validated.