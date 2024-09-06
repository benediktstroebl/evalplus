The following Python script offers a self-contained function that solves the problem of creating a palindrome from a given input string. 

```python
# Python program to find a palindrome
def is_palindrome(string):
  """ 
  Function to check if a given string is a palindrome or not. 
   Returns 1 if it, else 0 
 """
  if string == string[::-1]:
      return 1
  else:
      return 0 

def make_palindrome(string):
  """ 
  Function to make a palindrome from a given string.
  """ 
  Returns the Palindrome is a string that reads the same when reversed. 
  A palindrome is always begins with a non-palindrome character and ends with a palindrome 
  """
  if len(string) == 0:
      return ""
  elif len(string) == 1:
      return string
  else:
      # Find the longest postfix of supplied string that is a palindrome
      postfix = ""
      for i in range(1, len(string)):
         if string[i-1] == string[i]:
              postfix += string[i]
          else:
              break
      # Append to the end of the string reverse of a string prefix that comes before the palindrome
      return postfix + string[::-1]

# Driver code
print(is_palindrome(""))
print(is_palindrome("cat"))
print(is_palindrome("cata"))
print(make_palindrome(""))
print(make_palindrome("cat"))
print(make_palindrome("cata"))
```

This code has a function that checks whether a given string is a palindrome. It also has a function to create a palindrome from a given string. 

The make_palindrome function uses a simple algorithm to create a palindrome. It first checks for the Finally case, which is the simplest palindrome. 

It then uses a loop to find the longest postfix of the string that is a palindrome. It then appends the core to the end of the string, reversed from its prefix.