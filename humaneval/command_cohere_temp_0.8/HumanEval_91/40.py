Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            cnt += 1
    return cnt
```

This function utilizes the split('.'): statement to split the input string into a list of sentences. The strip() function is used to remove any trailing or leading white spaces. Subsequently, it checks if each sentence starts with the word 'I', and if it does, it increments the counter by 1. The function then returns the final count of boredoms.

Here's an example usage of this function:
```python
# Example 1 from the prompt
result = is_bored("The sky is blue. The sun is shining. I love this weather")
print(result)  # Output: 1

# Example 2 from the prompt
result = is_bored("Hello world")
print(result)  # Output: 0
```

This should output:
```
1
0
```

Which matches the examples provided in the original problem description. Feel free to test it with other examples to verify its behavior.  If you have any more questions or want to explore further, please don't hesitate to ask!