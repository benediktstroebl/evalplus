```python
def find_max(words):
    char_count = {}
    lexic_front = {}
    for word in words:
        unique_chars = len(set(word))
        if unique_chars not in char_count:
            char_count[unique_chars] = []
        char_count[unique_chars].append(word)
        lexic_front[unique_chars] = word

    return min(lexic_front, key=lexic_front.get)
```

The Python script provided defines a function called `find_max` that takes in a list of strings, specifically words. The purpose of this function is to identify the word within the list that contains the highest number of unique characters, with the preference of returning the word that appears first in lexicographical order among such words.

The function employs two dictionaries: `char_count` to keep track of the frequency of unique characters per word, and `lexic_front` to store words with the highest number of unique characters and their positions in lexicographical order.

Here's a breakdown of the function:
1. **Iteration** - The function loops through each word in the provided list.
   - For each word, the unique characters within that word are counted using the `set()` function to create a unique set of characters, and the length of this set gives the count of unique characters.
2. **Dictionary Population** - After counting the unique characters for each word, the function populates the `char_count` dictionary with these counts. This dictionary now holds the unique character counts as keys and lists of words with that count as values.
   - The function also populates the `lexic_front` dictionary, which stores words with the highest unique character count and prioritizes words that appear earlier in lexicographical order. 
 3. **Return Behavior** - The function returns the first word that appears in the lexicographical order among the words with the highest unique character count. This is ensured through the use of the `min()` function, combined with the `key` parameter, to minimize the `lexic_front` dictionary based on the lexicographical order of the words.

In summary, the provided script offers a clear and concise solution to the problem statement, efficiently identifying and retrieving the word from the list with the most unique characters, while prioritizing words that come first in lexicographical order.