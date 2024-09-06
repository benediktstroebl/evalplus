Here's the Python code to solve the problem:
```python
def count_upper(s):
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i].lower() in 'AEIOU':
            cnt += 1
    return cnt
```

This code defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices using a loop. It then returns the count.

To test this function, you can use the following code:
```python
test_cases = [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
    ('BBE', 1),
    ('AaBbCcDdEeFf', 2),
    ('#Hashtags', 0),
]

for test_case in test_cases:
    assert count_upper(*test_case) == test_case[1]
```

This code provides a variety of test cases to cover different scenarios and ensure the function `count_upper()` is correct.