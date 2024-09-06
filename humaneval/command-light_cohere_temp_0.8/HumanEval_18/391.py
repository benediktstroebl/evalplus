```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test case 1
print("Test Case 1: " , "how_many_times('aaa', 'a'))
# Output: 3

# Test case 2
print("Test Case 2: " , "how_many_times('aaaa', 'aa'))
# Output: 3

# Test case 3
print("Test Case 3: " , "how_many_times('abcde', 'abc'))
# Output: 3

# Test case 4
print("Test Case 4: " , "how_many_times('','abc'))
# Output: 4
```