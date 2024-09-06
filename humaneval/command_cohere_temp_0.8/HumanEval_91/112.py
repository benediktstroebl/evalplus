```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string by periods, strips any extra whitespace, and checks if each sentence starts with 'I'. If it does, it counts it as a boredom. It then returns the total count of boredoms.

You can test this function using the examples provided in the original prompt:
```python
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
``` 

Let me know if this resolves your problem or if you'd like further clarification.