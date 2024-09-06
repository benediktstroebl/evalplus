```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Tests
string = "aaaaaa"
substring = "a"
print("Count:", how_many_times(string, substring), ")"
print(how_many_times(string, substring))

string = "hello"
substring = "el"
print("Count:", how_many_times(string, substring), ")"
print(how_many_times(string, substring))

``` 
This Python code defines a function `how_many_times` that finds the count of occurrences of a given substring within a given string. The function uses a loop to iterate over each character of the string, and if a character matches the given substring, it increments the count. The function then returns the result of the count of occurrences of the substring.