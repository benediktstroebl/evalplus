```python
from typing import List
def longest(strings: List[str]):
    #return the longest string in the list
    return max(strings, key=len)
#tests
strings = ['a', 'b', 'c']
strings. print = ['a', 'bb', 'ccc']
strings. = ['a', 'bb', 'ccc']
longest(strings)
longest(strings[::-1])  #test the reversed list
longest(['a'])  #test empty list
longest(['a', 'bb', 'ccc'])  #test list with different lengths
print(longest(['aa', 'b']))  #test list with different characters
```
This code defines a function `longest` that takes a list of strings and returns the longest string from that list. It uses the max function with the `len` key as the selection function to find the maximum length. 

The `longest` function is then tested with a few input strings.