```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
test_1 = [ 'a', 'a' ]
test_2 = ['aaaa', 'aa']
test_3 = ['_', '_']

test_cases = [test_1, test_2, test_3]

for test in test_cases:
    print(how_many_times(*test))
```
The function `how_many_times` takes two parameters: a string and a substring. It uses a strings and an iterator over the string and checks if each character matches the substring. It returns the the how many times the string appears in the original string.