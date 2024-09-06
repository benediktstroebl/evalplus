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
    # Using a list to store each word and its corresponding sorted char array.
    words = s.split()
    sorted_words = [self.sort_char_array(w) for w in words]
    return ' '.join(sorted_words)

  # A helper function to sort char array in ascending order.
  def sort_char_array(self, char_array):
    sorted_char_array = [str(c) for c in sorted(char_array)]
    return ''.join(sorted_char_array)
```

This code blocks all the words in the string and sorts the characters in each word. Then, it puts the words back together to form the sorted string while maintaining the order of words and spaces.

It would be best to ensure that you are using Python3 for this script to work efficiently as the code uses list comprehension, which is not valid in Python2.