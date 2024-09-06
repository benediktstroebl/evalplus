```python
def find_max(words):
    char_count = {}
    lex = sorted(words, key=lambda x: (len(set(x)), x))
    for i in range(len(lex)):
        curr = set(lex[i])
        total_char = len(curr)
        unique_count = len(curr) - 1
        if unique_count not in char_count:
            char_count[unique_count] = []
        char_count[unique_count].append((total_char, lex[i]))
    max_index = max(char_count, key=lambda x: len(x[0]))[0]
    return lex[max_index][0]
```

The function uses a dictionary to count the number of unique characters in each word. This ensures the maximum number of unique characters. In the case of a tie, the algorithm sorts words lexicographically and returns the first one. To implement this, the function sorts the list of words using a lambda function that prioritizes word length and lexicographic order. Then, it uses maximum uniqueness and lexicographic ordering to determine the maximum word.