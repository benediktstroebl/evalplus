Here's a Python script that contains a function called anti_shuffle, designed to transform an input string by reordering its characters according to their ASCII values while preserving the positions of words and spaces in the original string:
```python
def anti_shuffle(s):
    # Split the input string into individual words
    words = s.split()
    # Initialize an empty string to build the ordered result
    result = ""
    
    # Iterate through each word in the input string
    for word in words:
        # Sort the characters of each word based on ASCII values
        sorted_word = ''.join(sorted(word))
        # Add the sorted word to the result string
        result += sorted_word + " "
    
    # Remove the extra space at the end of the result string
    return result.rstrip()
```

This code defines a function that takes an input string s and returns a string where each word is replaced by a new word composed of its characters sorted in ascending order based on ASCII values. The function preserves the order of words and spaces in the original string. It achieves this by first splitting the input string into individual words using the split() method. Then, it iterates through each word, sorts its characters alphabetically based on ASCII values using the sorted() function, and joins them back together to form a new word. The resulting sorted words are combined together with spaces in the original word order, creating the final output string. Finally, any extra spaces at the end of the result are removed using rstrip().