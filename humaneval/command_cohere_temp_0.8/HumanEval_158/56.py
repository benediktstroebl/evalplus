```python
def find_max(words):
    words.sort()
    max_set = set()
    for word in words:
        char_set = set(word)
        if len(char_set) > len(max_set):
            max_set = char_set
    return words[max_set == max_set].strip("\n")
```

The Python script solves the problem using the following approach:
1. The input `list of strings` is sorted in lexicographical order. This ensures that if there are multiple strings with the maximum number of unique characters, the correct answer is the first one in the sorted list.
2. A `set` is used to keep track of the unique characters of each word. For each word in the sorted list, we create a char `set`, and if this set contains more unique characters than the previous maximum, we update the maximum set.
3. Finally, we return the string contained in the maximum set.