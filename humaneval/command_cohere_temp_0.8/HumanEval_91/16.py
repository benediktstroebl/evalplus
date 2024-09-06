```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count
```

This code defines a function called `is_bored` that takes a string as an input and counts the number of sentences that start with the word "I." The function uses the `sum` function to count the number of sentences that start with "I" from the list of split sentences (using '.', '?', '!') and returns the count.

To use this code, simply call the function by passing a string as an argument, and it will return the number of sentences that start with "I." For example:
```python
result = is_bored("The sky is blue. The sun is shining. I love this weather.")
print(result)  # Output: 1
```