Below is a Python script with a self-contained function that solves the problem of finding the shortest palindrome using the algorithm:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        # Find the longest palindrome prefix
        palindrome = find_palindrome(string)
        
        # Append the palindrome and reverse the prefix
        return palindrome + string[len(palindrome):] + palindrome[::-1]

def find_palindrome(string):
    return ''.join() if not string else ''.join_(string)

def not_palindrome(string):
    return False

if __name__ == "__main__":
    # Test the functions
    print("Is ' inflammable ' a palindrome? Palindrome: ")
    print(is_palindrome('inam'))
    print("\nMake palindrome from ' INFLAMABLE '.")
    print(make_palindrome(' INFLAMABLE '))
    print("\nIs ' test ' a palindrome.")
    print(is_palindrome('test'))
    print("\nMake palindrome from '!@.-'.")
    print(make_palindrome('!.-'))
    print("\nIs '() a palindrome? Palindrome: ")
    print(is_palindrome('('))
    print("\nMake palindrome from 'abc-.'.")
    print(make_palindrome('abc-.'))
    print("\nIs 'abc--' a palindrome.")
    print(is_palindrome('abc--'))
```
The script provides a set of functions that include the function is_palindrome, which determines whether a given string is a palindrome, and the function make_palindrome, which creates the shortest palindrome using the algorithm.

The main function tests these functions with various inputs and outputs the results. The output will show whether the string is a palindrome or not and the result of making the palindrome.