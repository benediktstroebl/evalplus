```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    # Count occurrences of substring in the string
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
print("First String:", result1) 

string2 = " Hello World"
substring2 = "o"
result2 = how_many_times(string2, substring2)
print("Second String:", result2)
```