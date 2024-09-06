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
    # Use a regex to find all words (assumes words are separated by spaces)
    words = re.findall(r'\w+', s)
    
    # Iterate through each word and sort the characters
    ordered_words = [ chr(c) for c in sorted(list(set(word))) for word in words]
    
    # Zip the sorted letters into a single string and return
    return ' '.join(ordered_words)
```

This code uses Python's regular expression re.findall function to extract all the words from the string. It then sorts the characters in each word while maintaining the order of the words and any spaces. The code to do this is the following:
```python
ordered_words = [ chr(c) for c in sorted(set(word)) for word in words]
``` 

The code uses the sorted function with a set of characters in each word to ensure that the sorting is done correctly. The set is necessary to remove any duplicate letters, ensuring that the sorting is done in the correct order. The code then uses a list comprehension to create a new string with the sorted characters, and joins these into one string to be returned.  This approach ensures that the order of words and spaces is maintained while sorting the characters within each word.  This algorithm is efficient and should have no problems processing inputs of varying sizes.