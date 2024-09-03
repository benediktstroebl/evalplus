```python
def anti_shuffle(s):
    """
    Reorders the words in the input string such that the words are rearranged 
    based on their ASCII values while maintaining their relative order.

    Parameters:
        s (str): Input string with multiple words.

    Returns:
        str: Reordered string with words sorted by ASCII values.
    """
    words = s.split()
    sorted_words = [sorted(word, key=lambda x: x.lower()) for word in words]
    return ' '.join(sorted_words)
```