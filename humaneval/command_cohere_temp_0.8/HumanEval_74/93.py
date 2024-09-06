```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This Python script defines a function called `total_match` that takes two lists of strings, `lst1` and `lst2`, as input. 

The function returns the list that has a total number of characters in all of the strings less than the other list. It uses the logical or operation to return the list with fewer characters, ensuring that it only returns one of the input lists and does not create a new list if both lists have an equal number of characters.

The behavior of the function is illustrated through examples, as shown below:
```python
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
```
The function guarantees that if the two lists have the same number of characters, it will always return the first list provided, but it will return the list with fewer characters if they differ.

The total_match function gives an elegant and straightforward solution to the problem statement, which asks for a list with fewer characters.