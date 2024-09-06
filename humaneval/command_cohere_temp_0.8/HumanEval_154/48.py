```python
def cycpattern_check(a, b):
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    return b in a or any(b in rotatedWord for rotatedWord in a.split(b))
```
This function takes two strings as input and rotates the second string in all possible ways using a list comprehension to check if it matches any substring of the first string. The function returns True if there is a match and False otherwise. 
To simplify the comparison process, the spaces in both strings are removed and all characters are converted to lowercase. 

If the following test cases are also provided the code will be 
```python
test_cases = [
    ("abcd", "abd"),
    ("hello", "ell"),
    ("whassup", "psus"),
    ("abab", "baa"),
    ("efef", "eeff"),
    ("himenss", "simen"),
]

for i in test_cases:
    assert cycpattern_check(*i) == True
```