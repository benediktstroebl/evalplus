```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function with some examples
string1 = "aaa"
string2 = "aaaa"aa"
string3 = "abc"def"
print("Results for string1:", how_many_times(string1, string1)) 
print("\nResults for string2:", how_many_times(string2, string2))
print("\nResults for string3:", how_many_times(string3, string3))
 ```

This code defines a function that finds the frequency of a given substring in a given string. It uses a straightforward iterating to count the occurrences of the substring in the original string. This function is run it for the provided test cases.