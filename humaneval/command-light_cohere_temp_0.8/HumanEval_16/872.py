```python
def count_distinct_characters(string):
    return len([c for c in string.string() if c.isalpha()])
 distinct_char_count = len([char for char in string if not(char.isalpha())])
   
    return max(distinct_char_count, distinct_char_count)

# Testing code
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('123') == 4
assert count_distinct_characters('') == 4
assert count_distinct_characters(' Jerry ') == 4
assert count_distinct_characters('   ' ) == 4
``` 
This code defines a function **`count_distinct_characters`** that accepts a string **`string`** as an argument. The function employs two separate lists comprehension strategies to tally the distinct characters within the string and the distinct alphabet characters. 

This method provides an effective way to determine the number of unique characters in a given string.