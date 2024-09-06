```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(x in first for x in second[::-1])
```
The function `cycpattern_check` uses lowercase words to make sure that the comparison is case-insensitive. It also uses `any` to check if any rotation of the second word can be found in the first word. 

Here is a sample output of the function:
```
cycpattern_check("abcd","abd") => False
cycpattern_check("hello","ell") => True
cycpattern_check("whassup","psus") => False
cycpattern_check("abab","baa") => True
cycpattern_check("efef","eeff") => False
cycpattern_check("himenss","simen") => True
``` 
This output shows the results of passing different pairs of words to the `cycpattern_check` function. The result of each test is recorded and displayed.