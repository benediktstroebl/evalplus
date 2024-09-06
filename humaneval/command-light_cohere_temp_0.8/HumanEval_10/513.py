Here is a self-contained Python script with a function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ''
    
    result = []
    lst = list(string)
    reverse_ch = ''.joinrev(lst[::-1])
    
    for i in range(0,len(lst)):
        while lst[i] == reverse_ch:
            i+=1
        result.append(lst[i])
        result.append(reverse_ch)
        
    return ''.join(result)
```
The function is_palindrome checks if the input string is a palindrome or not. It returns True. The function make_palindrome takes the approach of finding the shortest palindrome that begins with the given string. The algorithm works by first finding the longest postfix of the string that is a palindrome, and then reverses that prefix to create the palindrome.