```python
def words_in_sentence(sentence):
    sentence = sentence.strip().split(' ')   
    words = []

    for word in sentence:
        if len(word) == 1:
            words.append(word)
        else:
            is_prime = True
            for num in range(2, int(len(word)**0.5)+1):
                if word%num == 0:
                    is_prime = False
                    break
            if is_prime:
                words.append(word)
                
    return ' '.join(words)
```

The given Python script defines a function `words_in_sentence(sentence)` that solves the problem. Here's a brief explanation of how it works:
1. The function first splits the input sentence into a list of words using spaces as separators.
2. It then initializes an empty list called `words` to store the words that have a length of 1 (these will be included in the output).
3. For each word in the sentence, if its length is not 1, the function checks if it's a prime number. This is done using an efficient primality testing approach called the `Sieve of Eratosthenes`.")
4.  If the word length is greater than 1 and it's a prime number, it's added to the `words` list.
5. Finally, the function joins the words back into a single string and returns the result, which is the sentence with only the words whose lengths are prime numbers.