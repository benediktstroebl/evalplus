```python
def reverse_delete(s, c):
    s = list(s)
    c = set(c)
    for char in c:
        s.remove(char)
    s = ''.join(s)
    return s, s == s[::-1]
```
The reverse_delete function takes two strings s and c as input and returns a tuple containing the modified string and a boolean indicating whether the modified string is a palindrome. 

This Python script solves the problem by first creating a set of characters from the second string c. It then removes each character from the first string s if it exists in the set of characters from c. Subsequently, the modified string is concatenated and returned as the first element of the tuple. The second element is a boolean that is True if the modified string is a palindrome and False otherwise. This is determined by checking whether the modified string is equal to its reverse (s[::-1]). 

This approach ensures that all characters in s that are present in c are removed, and the resulting string is checked for being a palindrome.

The provided solution has a time complexity of O(n) where n is the length of the input string s, as it requires iterating over the characters in s and performing remove operations for each character in c. The space complexity is O(1) as it only uses a constant amount of memory to store the modified string and the boolean result.