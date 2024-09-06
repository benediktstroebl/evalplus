Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to consider
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

To test the functionality, you can add tests to ensure the function behaves as expected:
```python
# Test case 1
test_str = 'aBCdEf'
expected = 1
result = count_upper(test_str)
assert result == expected, f'Expected {expected}, but got {result}'

# Test case 2
test_str = 'abcdefg'
expected = 0
result = count_upper(test_str)
assert result == expected, f'Expected {expected}, but got {result}'

# Test case 3
test_str = 'dBBE'
expected = 0
result = count_upper(test_str)
assert result == expected, f'Expected {expected}, but got {result}'
```

This script will pass those tests and provide the desired count of uppercase vowels in even indices of the given string. 
If you encounter any issues or have further questions, feel free to ask for assistance!