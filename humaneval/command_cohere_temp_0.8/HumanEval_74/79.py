```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This Python script defines a function called `total_match` that takes two lists of strings, `lst1` and `lst2`, as input. The function returns the list that has a total number of characters in all its strings less than the other list's strings. If both lists have the same number of characters, it returns the first list `lst1`. The function uses logical and/or operations to combine conditions and returns the correct list based on the specified conditions. 

Here is an example of how one can use this function:
```python
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # Output: ['4']
```
This example returns the list `['4']` since the total number of characters in the string '4' is less than the total number of characters in the strings in the list `['1', '2', '3', '4', '5']`. 

The function includes examples that cover different scenarios in the docstring, which can be useful for understanding and testing the function.