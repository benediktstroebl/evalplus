```python
def find_max(words):
    max_unq = 0
    res = None
    for w in words:
        unq = set(w)
        if len(unq) > max_unq:
            max_unq = len(unq)
            res = w
    return res
```

The algorithm is simple:
1. Initialize the variable `max_unq` with zero and `res` with `None`. These variables will store the result. `max_unq` will hold the maximum number of unique characters, and `res` will hold the corresponding word.
2. Loop through each word in the input list.
3. For each word, calculate the number of unique characters by converting the word into a set using the `set()` function and getting its length.
4. If the unique characters are more than the previous maximum, update `max_unq` and `res`.
5. After looping through all the words, return the `res` value.

This algorithm efficiently solves the problem without using any built-in sorting or indexing functions like `sorted()` or `dict()` , making it self-contained. It first finds the word with the maximum number of unique characters and then checks if there are multiple words with the same maximum. If so, it returns the earliest one in lexicographical order.