```python
def words_in_sentence(sentence):
    """
    Returns a string containing words from the input sentence whose lengths are prime numbers,
    preserving the original order.
    """
    prime_words = []
    words = sentence.split()

    for word in words:
        length = len(word)
        if length > 1 and all(length % i for i in range(2, length)):
            prime_words.append(word)

    return ' '.join(prime_words)
```