```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aaaaaaab"
string4 = "iiii"

print("Test 1:", how_many_times(string1, string2)") 
print("\n\n")
print("Test 2:", how_many_times(string3, string2)") 
print("\n\n")
print("Test 3:", how_many_times(string4, string2)")
print("\n\n")

# Example of_many_times() result
print("The number of times 'aa' can be found:", how_many_times(string1, 'aa'))

``` 
This Python script defines a function `how_many_times` that takes two parameters: a string and a substring. The function uses a a loop to iterate over each character in the string, and counts the number of times the substring appears. The function then returns the the number of times the substring appears in the original string.