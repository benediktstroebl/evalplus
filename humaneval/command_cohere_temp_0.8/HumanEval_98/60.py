Here's a Python script that contains a function named `count_upper()` which solves the problem as outlined in the markdown code block you provided:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function takes a string s as input and calculates the number of uppercase vowels it contains in every even index of the string. The function then returns the total count of uppercase vowels in the even indices. 

You can use this function by calling it and passing the required string as an argument as demonstrated in the main section of the script:
```python
# Main section
string = 'aBCdEf'
result = count_upper(string)
print("Count of uppercase vowels in even indices:", result)
```

This will output:
Count of uppercase vowels in even indices: 1

Which is the correct answer for the given example string 'aBCdEf'.