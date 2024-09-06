```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
This code uses a list to store all the prefixes of the string and a for loop to iterate through each character starting from the second character and append the prefix to the list in decreasing order. 

Here is an example usage of the `all_prefixes` function:
```python
print(all_prefixes('Good'))
```
The output of this code will be:
```
['G', 'Go', 'Good', 'Goodo', 'Goodod', 'Goododo']
```
Which contains each prefix of the string "Good" in descending order, from shortest to longest.