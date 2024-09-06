```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([c for c in txt if c.islower() and ord(c) % 2 == 0])
    return words
```

The provided Python script defines a function called `split_words` that takes a string as input. This function is designed to split the input string into words based on whitespace or commas, or if these delimiters are absent, it returns the count of lowercase letters with even ASCII values.

Here's a breakdown of how the function works:
1. `words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([c for c in txt if c.islower() and ord(c) % 2 == 0])`: This line employs conditional logic to determine how to split the input string into words. The function checks for the presence of commas (`','`), spaces (`' '`), or lowercase letters with even ASCII values. Here's the breakdown of each condition:
     - If commas are present in the string (`','` is in `txt`), the string is split using commas as separators, resulting in the words being separated by commas. This is done using the `split` method with `','` as the argument.
     - If commas are not present but spaces are in the string (`' '` is in `txt`), the string is split using spaces as separators, which is also done using the `split` method with `' '` as the argument.
     - If neither commas nor spaces are present, the function counts the number of lowercase letters with even ASCII values. This is achieved by using a list comprehension that iterates through each character in the string, checking if it's lowercase and if its ASCII value is even (using the `ord` function and the modulo operator `%`).
     - The result of this count is then returned as the output of the function.
2. `return words`: Finally, the function returns the resulting words after splitting the input string or the count of lowercase letters with even ASCII values, depending on which condition is satisfied.

This code showcases an example of how to write flexible code that can handle a variety of input conditions using if-else statements and conditional expressions.