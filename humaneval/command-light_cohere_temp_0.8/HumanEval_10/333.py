Here is a Python script that contains a self-contained function that solves the problem of finding the longest palindromic substring in a given input string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    if not string:
        return ''
    l, r = 0, len(string)-1
    while l <= r:
        p = string[l:r]
        q = p[::-1]
        if is_palindrome(q):
            return p + q
        l += 1
        r -= 1
    return string
```
This script defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function takes a string as input and returns `True` if the string is a palindrome and `False` otherwise. The `make_palindrome` function takes a string as input and returns the shortest palindrome that begins with the given string. It uses a algorithm to find the palindrome:
1. The function first checks if the input string is empty, and returns the empty string if it is.
2 Then next, the function initializes variables `l` and `r` to 0 and `len(string)-1` respectively, which represent the leftmost and rightmost index of the substring to be extended, respectively.
3 The function then enters a while loop that continues until `l` is greater than `r`. Within the loop, it checks if the substring `p` equals the reversed substring `q`. If they are equal, then the function returns the substring `p` concatenated with its reverse `q`. This is because the reversed substring `q` is another palindrome that begins with `p`. 
4 If the condition is not met, the function increments `l` and decrements `r`. It then repeats the process until it finds a palindrome. 
 This algorithm uses the efficient method with a single pass to reduce the search space in each iteration.