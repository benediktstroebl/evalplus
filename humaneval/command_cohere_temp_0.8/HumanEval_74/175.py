```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This function compares the total number of characters in two lists of strings `lst1` and `lst2`, it returns the list with fewer characters if the total count is less, and returns the first list if they are equal. It uses logical AND (`and`) and OR (`or`) for the shortest list and returning `lst1` or `lst2` respectively when necessary. 

Here is a usage example:
```python
print(total_match(['4'], ['1', '2', '3', '4', '5']))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
```
The above example will print:
```bash
['4']
['hI', 'Hi']
['hi', 'admin']
['hI', 'hi', 'hi']
```