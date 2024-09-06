Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            count += 1
    return count
```

This script defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. A boredom is defined as a sentence that starts with the word "I". The function iterates over the string splitting it on periods, strips each sentence, and checks if the sentence starts with "I" and does not include an exclamation mark '!' or a question mark '?'. The total number of boredoms is counted and returned.

To test this script, you can call `is_bored` with different inputs to verify the function's behavior:
```python
# Test Case 1
input1 = "The sky is blue. The sun is shining. I love this weather"
result1 = is_bored(input1)
print(f"Test Case 1: {result1} ")

# Test Case 2
input2 = "Hello world"
result2 = is_bored(input2)
print(f"Test Case 2: {result2} ")

# Test Case 3
input3 = "I am bored. What a boring day. I am going to sleep."
result3 = is_bored(input3)
print(f"Test Case 3: {result3} ")
```

This will yield the following output:
```
Test Case 1: 1
Test Case 2: 0
Test Case 3: 2
```

This shows that the `is_bored` function correctly counts the number of boredoms in a given input string.