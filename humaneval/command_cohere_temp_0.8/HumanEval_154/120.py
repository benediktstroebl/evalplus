```python
def cycpattern_check(a, b):
    s = set()
    s.add(a)
    s.add(b)
    for i in range(len(a)):
        s.add(a[i:] + a[:i])
    return b in s or b == a
    # Tests:
    # cycpattern_check("abcd","abd") => False
    # cycpattern_check("hello","ell") => True
    # cycpattern_check("whassup","psus") => False
    # cycpattern_check("abab","baa") => True
    # cycpattern_check("efef","eeff") => False
    # cycpattern_check("himenss","simen") => True
```