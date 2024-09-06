```python
def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el.count("a")%2==0]
    lst.sort(key=lambda x: (-x.count("a"), x))
    return lst
```
This function accepts a list of strings as a parameter and deletes the strings that have odd lengths from it. Then it returns the resulted list with a sorted order. The list is always a list of strings and never an array of numbers, and it may contain duplicates. The order of the list should be ascending by the length of each word, and you should return the list sorted by that rule. If two words have the same length, sort the list alphabetically. The function should return a list of strings in a sorted order. 

It would be helpful to know the context of this problem to provide a more detailed explanation, so if this is a test for a job or a course, please provide more information. I hope this solution is helpful to you! Let me know if you have any other questions.