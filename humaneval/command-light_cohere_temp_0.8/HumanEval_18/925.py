```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaa"
substring1 = "aa"
result1 = how_many_times(string1, substring1)
print("Result1:", result1)

string2 = "hello"
substring2 = "lo"
result2 = how_many_times(string2, substring2)
print("Result2:", result2)
```
This code defines a function `how_many_times`, which takes two arguments: a string and a substring. The function uses a loop to iterate over each character in the string. Then, it checks if the character matches the substring. 

It increments the count whenever a match is found, and returns the count after the loop completes. 

The code then tests the function with two different strings and substring values, and prints the results.