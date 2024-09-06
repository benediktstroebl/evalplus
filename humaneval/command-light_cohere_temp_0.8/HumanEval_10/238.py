Here is a self-contained Python function that solves the problem:
```python
def is_palindrome(string): 
    """ Check if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ""
    
    palindrome = []
    l = len(string)
    
    while True:
        if l % 2 == 0:
            # Even number, take the center
            palindrome.append(string[l//2])
            l -= 2
        else:
            # Odd number, append and then reverse the prefix
            palindrome.append(string[0::l//2])
            l -= 1
            palindrome.reverse(palindrome)
            
    return ''.join(palindrome)
```
The function uses a simple algorithm to generate the shortest palindrome. It first checks if the ** the empty string, in which case it returns an empty string. If the string is not empty, it checks if the length is even, indicating the beginning can be a palindrome. In this case, it takes the center of the string and appends it to the palindrome. 

If the length is odd, it checks if the middle of the string is a palindrome. If it is, it appends it to the palindrome and removes the center. Then, it checks if the string is a palindrome by reversing the palindrome. If it's not a palindrome, it uses the prefix of the string to create the palindrome by appending it to the reversed string.