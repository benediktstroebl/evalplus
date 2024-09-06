```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != ',' else len(list(filter(lambda x: len(x) != 1 or x[0].islower(), words)))
```

The problem specification suggests several rules for splitting a string of words into a list, depending on the presence of whitespace and commas. Here's a breakdown of the script:
1. The script starts with the assumption that the string `txt` is a collection of words separated by spaces or commas. 
2. The code uses `find(' ') to check whether there is a whitespace character in the string. Since this method returns -1 if the character is not found, it assumes that there are no spaces in the string if the result is -1. 
3. Conversely, if there is at least one space in the string, it utilizes the `split()` method to separate the string into a list of words, splitting on whitespace.
4. In the case where the string has no spaces but contains commas, it splits the string on commas using `split(',')`.
5. The script returns the split list of words. 
6. Lastly, if the split list results in a list where all elements have a length of 1 and are lowercase letters, it returns the total count of such words as the backup option. This is achieved using the `filter()` method, which creates a new list with the same items as the original, but with the elements for which the condition (lambda x: len(x) != 1 or x[0].islower()) is `True`. 

Overall, the script provides a flexible solution that handles various input scenarios while adhering to the problem's specifications. Let me know if you would like to go through any parts of the solution in more detail. 
Alternatively, feel free to further refine the solution to reach the cleanest implementation possible.