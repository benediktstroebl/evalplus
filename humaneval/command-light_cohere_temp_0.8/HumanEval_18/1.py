Here is a self-contained Python function that solves the problem of counting the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test cases
test_1 = ["a", "aaa", "aaaa"]
test_2 = ["", "aa", "aaa"]
test_3 = ["hello", "el","lo"]
test_4 = ["a", "aaa", "aaaa"]

# Function call
res1 = how_many_times("hello", "el")
res2 = how_many_times("aaaa", "aa")
res3 = how_many_times("abc", "bc")
res4 = how_many_times("xxxx", "xxy")

print(f"Reservations:")
print(res1)
print(res2)
print(res3)
print(res4)
```

This function takes two parameters: string, which is the original string, and substring, which is the substring to search for. The function then uses a loop to iterate over each character in the substring and checks if each character is present in the string. The number of times the count variable is incremented for each character that is found. The function returns the number of times the substring appears in the original string.