```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aaaaaaa"

print("Result for string1:", how_many_times(string1, string1))
print("Result for string2:", how_many_times(string2, string2))
print("Result for string3:", how_many_times(string3, string3))
 ```

The code defines a function that returns the count of a given substring in a string. It employs a loop that iterates through every character in the string and checks if the current character is equal to the given substring. It then counts the necessary time a character is found, and returns the count. The function is then tested with three different strings and the results are printed out.