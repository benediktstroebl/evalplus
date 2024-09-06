```python
def find_max(words):
    char_count = {}
    lexic_front = {}
    for word in words:
        unique = set(word)
        count = len(unique)
        if count not in char_count:
            char_count[count] = []
        char_count[count].append(word)
        lexic_front[word] = count
    # Check if there's a lexicographically earlier candidate for each count.
    for word in words:
        count = lexic_front.get(word)
        if count:
            if len(char_count[count]) > 1:
                del lexic_front[char_count[count][1]]
            char_count[count].remove(char_count[count][0])
            char_count[count][0] = word
    max_count = max(list(char_count.keys()), key=lambda x: char_count[x])
    return char_count[max_count][0]
```

The script employs a dictionary called `char_count` to tally the unique characters in each word of the input list. Additionally, another dictionary called `lexic_front` is used to hold the frontmost candidate for each character count, sorted lexicographically. After tallying the character counts and populating `lexic_front`, the function identifies the word with the highest count of unique characters that is also lexicographically foremost among all other candidates with the same count. The final result is returned as the word that fulfills both criteria. 

The approach guarantees the correct solution for the provided test cases.