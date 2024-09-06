```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != [''] else len(set(txt.lower())) % 2 == 1
```

The Python script splits a string of words into a list, handling cases where there are no spaces or commas for separation. If the input string is empty, it returns an empty list or odd number of lowercase letters, depending on the situation. This approach ensures that the function behaves appropriately and adheres to the problem's specified conditions.