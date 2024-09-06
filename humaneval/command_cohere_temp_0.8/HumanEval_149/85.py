```python
def sorted_list_sum(lst):
    lst_new = []
    for i in lst:
        if len(i) % 2 == 0:
            lst_new.append(i)
    lst_new.sort()
    for i in range(len(lst_new)-1):
        if lst_new[i] < lst_new[i+1]:
            return lst_new
    return lst_new
```
The method utilizes a simple iterative approach to solve the problem. It iterates through the list of strings (lst), and adding to the new list (lst_new) only the strings that have even lengths. Afterwards, it sorts the new list using the .sort() method, and finally, it returns the new list in an ascending order.

The function passes the test cases provided in the prompt, as it sorts the list according to the rules described. 

For example:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```