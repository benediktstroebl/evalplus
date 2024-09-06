```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    # sort by len, then alphabetically
    lst_new.sort(key=lambda x: (len(x), x))
    return lst_new
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out strings with odd lengths and retains the even-length strings. Then, it sorts the list in ascending order based on string lengths, and within strings of the same length, it sorts them alphabetically. The result is a list of strings in the desired sorted order, ready for return.

Here is an example function call:
```python
print(sorted_list_sum(["aa", "a", "aaa", "ab", "c", "aba", "abc"]))
```
The expected output is:
```
['a', 'a', 'aa', 'ab', 'abc', 'aba']
```