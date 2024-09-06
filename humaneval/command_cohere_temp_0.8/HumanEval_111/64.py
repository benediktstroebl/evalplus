```python
def histogram(test):
    letters = test.split()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```
The code works by first splitting the input string into letters and then using a dictionary to count each letter's occurrence. The solution is case-insensitive, assuming the input contains only lowercase letters.

To use this code simply call the `histogram()` function with the `test` string as an argument like this: 

```python
print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
``` 

This will print the resulting histogram as a dictionary.