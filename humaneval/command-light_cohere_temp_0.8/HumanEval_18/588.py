```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

#Test case 1
print(how_many_times("aaa", "aa"))
# Expected output: 3

#Test case 2
print(how_many_times("abc", "ab"))
# Expected output: 2

#Test case 3
print(how_many_times("aaaa", "aa"))
# Expected output: 3

#Test case 4
print(how_many_times("abcde", "ab"))
# Expected output: 1

#Test case 5
print(how_many_times("hello world", "world"))
# Expected output: 3
```