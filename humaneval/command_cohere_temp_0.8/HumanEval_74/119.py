```python
def total_match(lst1, lst2):
    # Calculate the total character count in lst1 and lst2
    total1 = sum(len(val) for val in lst1)
    total2 = sum(len(val) for val in lst2)

    # If the total character count of lst2 is less than lst1, return lst2
    if total1 > total2:
        return lst2
    # If the total character count of lst1 is less than lst2, return lst1
    elif total2 > total1:
        return lst1
    # If the total character counts are the same, return the lexicographically smaller list
    else:
        return min(lst1, lst2)
```

This function compares the total number of characters in both lists and returns the list with fewer total characters. If both lists have the same number of characters, it returns the list that comes first in lexicographical order. The unit tests demonstrate the function's behavior on various input examples. 
```python
test_total_match = [(([], []), []),
                    ((['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi']),
                    ((['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin']),
                    ((['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi']),
                    ((['4'], ['1', '2', '3', '4', '5']), ['4'])]
```
The expected output of the tests is also provided for evaluation. It's important to note that this solution relies on the lexicographical ordering rule, which gives the impression that is followed by the built-in Python sorting mechanism. Nevertheless, explicitly sorting the lists may be slower for lengthy lists. 

If performance is an issue, considering alternative optimization techniques or indexing schemes may be beneficial.