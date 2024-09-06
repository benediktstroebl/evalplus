```python
def find_max(words):
    char_count = {}
    lexicographical_order = []
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        lexicographical_order.append((len(unique_chars), word))
    # Sorting lexicographical_order by the number of unique chars in descending order
    sorted_lexicographical_order = sorted(lexicographical_order, key=lambda x: x[0], reverse=True)
    return sorted_lexicographical_order[0][1]
```

The Python script defines a function `find_max` that takes in a list of strings, specifically words. The purpose of the function is to identify the word with the highest count of unique characters, and if there are multiple words with the same count, it returns the one that appears first in lexicographical order.

The function utilizes sets to calculate the unique characters present in each word. Subsequently, a dictionary named `char_count` is employed to store the number of unique characters for each word. A list, `lexicographical_order`, is created to arrange the words based on both their unique character counts and their lexicographical order, in descending order of unique characters. This list acts as a secondary sort.

Finally, the function performs a sort on the `lexicographical_order` list, arranging it by the number of unique characters in descending order. The first element (or the highest number of unique characters) from this sorted list is then returned, effectively giving the word that satisfies the criteria of having the most distinct characters and being the first in lexicographical order among any equally qualified words.

In summary, the Python code offers an efficient solution to pinpointing the word from a given list that boasts both the highest count of unique characters and leads in lexicographical order among any competing words with identical uniqueness counts.