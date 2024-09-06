Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            count += 1
    return count
```

This function counts the number of boredoms in a given string `S` by splitting the string into sentences using the delimiter '.' and checking if each sentence starts with the word 'I'. The function returns the total count of boredoms in the given string. 

The script can be tested as follows:
```python
# Test case 1
S1 = "The sky is blue. The sun is shining. I love this weather"
print(is_bored(S1))  # Output: 1

# Test case 2
S2 = "Hello world"
print(is_bored(S2))  # Output: 0
``` 

This will yield the correct output of 1 for the first test case and 0 for the second. 
If needed, you can incorporate more tests to cover a broader range of scenarios and validate the function's correctness.  Feel free to ask any questions or provide additional information that you think might help improve this solution.