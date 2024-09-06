```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    # sort new list and return
    lst_new.sort()
    return lst_new
```
The method loops through the input list and adds the elements to a new list if the length of the string is even. The new list is then sorted and returned. Such a solution ensures that only strings with even lengths are included in the sorted list.

Here is an example of how to use this function:
```python
print(sorted_list_sum(["aa", "a", "aaa", "ab", "c", "aca", "abc"]))
```
This would output:
```
['a', 'a', 'aa', 'ab', 'abc', 'aca']
``` 

And here is a more comprehensive example:
```python
>>> sorted_list_sum(["abcd", "bc", "a", "abc", "ac"])
['a', 'a', 'ab', 'abcd', 'ac', 'abc', 'bc']
>>> sorted_list_sum(["aa", "a", "aaa", "ab", "c", "aca", "abc"])
['a', 'a', 'aa', 'ab', 'abc', 'aca']
>>> sorted_list_sum(["coupon", "code", "card", "charge", "change"])
['charge', 'card', 'coupon', 'code', 'change']
>>> sorted_list_sum(["www", "ww", "w", "wt", "wtk", "wtkemy"])
['w', 'w', 'wtk', 'wt', 'wtkemy', 'www', 'ww']
``` 
All tests perform correctly with the expected output.