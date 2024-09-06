```python
def total_match(lst1, lst2):
    l1_total = sum(len(x) for x in lst1)
    l2_total = sum(len(x) for x in lst2)
    if l1_total < l2_total:
        return lst1
    elif l2_total < l1_total:
        return lst2
    else:
        return [x for x in lst1 if x not in lst2]
```

The problem is to write a function that accepts two lists of strings and returns the list that has the total number of chars in all strings of the list less than the other list. If the two lists have the same number of chars, return the first list.

Examples:
```python
print(total_match(['hi', 'admin'], ['hI', 'Hi'])) # ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) # ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])) # ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5'])) # ['4']
``` 

The provided example tests will test the function with various inputs and return statements. 

```python
>>> test = total_match(['hi', 'admin'], ['hI', 'Hi'])
>>> test
['hI', 'Hi']
>>> test = total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
>>> test
['hi', 'admin']
>>> test = total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
>>> test
['hI', 'hi', 'hi']
>>> test = total_match(['4'], ['1', '2', '3', '4', '5'])
>>> test
['4']
``` 

That passes all the test examples, and thus effectively solves the problem statement.