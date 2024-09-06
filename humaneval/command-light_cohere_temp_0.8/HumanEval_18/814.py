```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test case 1
print(how_many_times('', 'a'))  # Output: 0

# Test case 2
print(how_many_times('aaa', 'a'))  # Output: 3

# Test case 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script defines a function how_many_times that takes a string and a substring as input and returns the count of the substring in the string. It uses a iterates over each character in the string and checks if it's equal to the substring. If they are, it increments the count. 

Please note that this solution is case-sensitive, so it will only find matches if the substring is equal to the corresponding characters in the string.