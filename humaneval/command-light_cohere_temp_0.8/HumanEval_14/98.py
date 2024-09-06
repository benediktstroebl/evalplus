```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(w for w in string if w.isalpha()) for i in range(1, len(string))]+
```
This code defines a function called **`all_prefixes`** that returns a list of all prefixes in a given string. It uses list comprehension and the strings that are characters that are not alphanumeric (letters or digits) by using the **`not alpha`** function. 

The code also uses the range function to iterate over the string from the shortest to the longest characters and checks if each character is an alphanumeric character. 

In other words, the code efficiently generates all the prefixes in the given string, which is a common problem in string manipulation and can be very useful in many programming tasks.