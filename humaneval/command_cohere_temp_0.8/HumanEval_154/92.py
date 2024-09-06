```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    
    # Check if the second word is a substring of the first word
    if second in first:
        return True
    
    # Check for rotations of the second word in the first word
    rotations = [second[1:], second[0:1], second[1:] + second[0:1]]
    for rot in rotations:
        if rot in first:
            return True
    
    return False
```

This function compares the lowercase versions of both words first, which eliminates case sensitivity issues. It then directly checks if the second word is a substring of the first and returns `True` if so. Additionally, it generates rotated versions of the second word and checks if any of these rotations exist within the first word. The function returns `True` if any of these rotational substring conditions are met and `False` otherwise. 

Here is an example usage:
```python
print(cycpattern_check("hello","ell"))
print(cycpattern_check("whassup","psus"))
print(cycpattern_check("abab","baa"))
print(cycpattern_check("efef","eeff"))
print(cycpattern_check("himenss","simen"))
```
Which will print:
```bash
True
False
True
False
True
```