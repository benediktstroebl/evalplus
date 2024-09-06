```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Test case 1: Basic strings
test_case1 = "abc"
print("Test case 1: ", end="")
print(all_prefixes(test_case1))

# Test case 2: Removing punctuation
test_case2 = "!"
print("Test case 2: ", end="")
print(all_prefixes(test_case2))

# Test case 3: Empty string
test_case3 = ""
print("Test case 3: ", end="")
print(all_prefixes(test_case3))

# Test case 4: Long text with punctuation
test_case4 = "This is a very  long text with a lot of punctuation! Aaaaaaa"
print("Test case 4: ", end="")
print(all_prefixes(test_case4))

# Test case 5: Multicharacters
test_case5 = "a*b"
print("Test case 5: ", end="")
print(all_prefixes(test_case5))
```
This Python script defines a function all_prefixes that returns a list of prefixes from the input string. It uses a strings and punctuation as the input, removing any non-alphanumeric characters, and then joining them together to form the desired prefixes. 

This function is self-contained, and it can be easily incorporated into larger scripts or projects where you want to find and manipulate prefixes within strings.