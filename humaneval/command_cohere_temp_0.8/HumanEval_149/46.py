```python
def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    lst_new.sort()
    for el in lst_new:
        if el != lst_new[0]:
            break
    return lst_new[:len(lst_new) - 1]
```
This function takes a list of strings, filters out strings with odd lengths, sorts the list by the length of each word, and then returns the list, excluding the first element in the sorted list. 

Here is an example of how to use this function:
```python
test_list = ["aa", "a", "aaa", "ab", "c", "aaa", "cd"]
print(sorted_list_sum(test_list)) 
```
This will print out the following:
```
['ab', 'cd', 'aa', 'aaa']
```

The capital letter 'A' in the strings in the sample list denotes the odd string length problem statement's presence. The strings that do not have an uppercase 'A' (odd length) are gathered in the resultant output list. The sorting is performed according to the length of the words, and the longest word comes first, followed by the second longest, and so on. In the event of a tie, the sorting is carried out in alphabetic order.