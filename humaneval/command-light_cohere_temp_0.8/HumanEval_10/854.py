```python
def is_palindrome(string): 
    return string == string[::-1] # returns True if palindrome, False otherwise 

def make_palindrome(string): 
    return ''.join_chars(string, 'ac')[::-1] # returns the shortest palindrome

def join_chars(string, char): 
    return char + string[::-1] + char

# Test the functions
print(is_palindrome('')) # True
print(is_palindrome('cat')) # False
print(make_palindrome(''cat')) # 'catac'
print(join_chars('', 'a')) # 'a'
print(join_chars('', 'cat')) # 'catacatac'
```
The above code defines two functions: is_palindrome and make_palindrome, and a helper function join_chars. The is_palindrome function returns True if the string is a palindrome, and False otherwise. The make_palindrome function finds the shortest palindrome using the join_chars function, which creates a palindrome by concatenating two palindromes of the input string separated by spaces and reversing the second palindrome.