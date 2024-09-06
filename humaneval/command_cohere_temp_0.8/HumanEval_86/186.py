Here's a Python script with a self-contained function that solves the problem:
```python
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Iterate over each word and sort each word separately
    result = ' '.join(char_sorted(word) for word in s.split(' '))
    
    # If the input string ends with a space, we need to add it to the end of the result
    if s.endswith(' '):
        result += ' '
    
    return result

def char_sorted(word):
    """
    Sort characters in word from smallest to largest
    """
    return ''.join(sorted(word))

# Test cases
print(anti_shuffle("Hi")) # Should return "Hi"
print(anti_shuffle("hello")) # Should return "ehllo"
print(anti_shuffle("Hello World!!!")) # Should return "Hello !!!Wdlor"
```

This code defines the anti_shuffle function, as described in the problem statement. The char_sorted function is used within anti_shuffle to sort characters within each word. This code should produce the desired output for the given test cases. Feel free to add more tests or modify the function as needed. Let me know if you have any more questions or if you'd like to explore other concepts related to sorting and data manipulation in Python!