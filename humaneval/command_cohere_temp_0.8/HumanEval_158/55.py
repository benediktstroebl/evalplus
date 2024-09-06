```python
def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for w in words:
        uniq = len(set(w))
        if uniq > max_uniq:
            max_uniq = uniq
            result = w
    return result
```

The function uses a loop to iterate through each word in the list, calculating the number of unique characters in each word using the `set` function and comparing this quantity to a running maximum. The word that maximizes the number of unique characters and meets the lexicographical criterion is returned.

This approach is efficient because it assumes that the list is already sorted, which the prompt states. If the list is not sorted, there is an O(n log n) penalty for sorting the list. Let's assume that the list is always sorted for the problem statement.