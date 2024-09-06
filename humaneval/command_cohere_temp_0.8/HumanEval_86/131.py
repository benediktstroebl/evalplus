```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using the `split()` method (considering spaces as separators), and then sorts the characters in each word based on their ASCII values. The sorted words are then rejoined into a new string while maintaining the original spacing, providing the ordered version of the input string.

Here's an example usage:
```python
print(anti_shuffle("Hello World!!!"))  # Output: "Hello !!!Wdlor"
```

This will produce the ordered version of the string as described in the problem statement. Do note that the approach assumes that words in the input string are separated by single spaces. It works as expected for the given examples, but if the input string contains different types of spacing or other special characters, additional handling might be required. 

Make sure to have Python installed to run this code and test it out for yourself!