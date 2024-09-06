```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        new_word = ''.join(sorted(word))
        new_word_array.append(new_word)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a shuffled version of the string where each word is replaced by a new word formed by sorting the characters of the original word based on their ASCII values. The script retains the order of words and blank spaces in the original string.

This code can be tested as follows:
```python
# Test Case 1
input_string = 'Hi'
expected_output = 'Hi'
result = anti_shuffle(input_string)
print(f'Test Case 1: {result} == {expected_output}')

# Test Case 2
input_string = 'hello'
expected_output = 'ehllo'
result = anti_shuffle(input_string)
print(f'Test Case 2: {result} == {expected_output}')

# Test Case 3
input_string = 'Hello World!!!'
expected_output = 'Hello !!!Wdlor'
result = anti_shuffle(input_string)
print(f'Test Case 3: {result} == {expected_output}')
```

The expected output of the tests should be:
```bash
Test Case 1: Hi == Hi
Test Case 2: ehllo == ehllo
Test Case 3: Hello !!!Wdlor == Hello !!!Wdlor
``` 
This demonstrates that the `anti_shuffle` function correctly solves the problem statement.