The function is_palindrome(string: str) does the following:
- Checks if a given string is a palindrome.
- Returns True if it is a palindrome.

The function make_palindrome(string: str) solves the problem by finding the shortest palindrome that begins with a supplied string.

This algorithm idea is simple:
- Find the longest postfix of the supplied string that is a palindrome.
- Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

This approach guarantees to find the shortest palindrome that begins with the given string.