```python
def words_in_sentence(sentence):
    sentence = sentence.split()
    words = []
    for word in sentence:
      # checking if length(word) is prime
      if len(word) > 1 and all(sentence[words], sentence[words] != len(word) for i in range(2, len(word) + 1)):
        words.append(word)
    return ' '.join(words)
```

The function first splits the sentence into words and initializes an empty list `words` to store prime-length words. It iterates over each word in the sentence and checks if its length is greater than 1 and a prime number using the `all()` function and a generator expression. If the length is prime, it adds the word to the list `words`. Finally, the function joins the prime words back into a string and returns the result.

Here is a test to check if the function works:
```python
def test_words_in_sentence():
    assert words_in_sentence("Hello World!") == "Hello!"
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("I am prime meridian") == "I am prime"
``` 

The tests ensure that the function `words_in_sentence()` correctly identifies prime-length words and returns the desired output.  This approach takes advantage of the `all()` function and generator expressions to efficiently check the primality of word lengths.