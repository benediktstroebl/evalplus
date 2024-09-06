This is a solution to the Palindrome problem that generates the shortest palindrome starting with the input string. 

```python
def is_palindrome(string):
    """ returns True if string is a palindrome, False otherwise """
    if len(string) < 2:
        return False
    s1 = string[:]
    s2 = string[-1:]
    for i in range(len(string)//2):
        if s1[i] != s2[i]:
            return False
    return True
def make_palindrome(string):
    """ returns the shortest palindrome of a string """
    if not is_palindrome(string):
        return ""
    ans = ""
    while True:
        mid = len(ans)+1
        if is_palindrome(ans+string[0:mid]):
            break
        ans += string[0:mid]
    return ans[::-1] + ans[1:]
```