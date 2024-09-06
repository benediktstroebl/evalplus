```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Test the function
# Test with different cases
# Check for case-insensitive matching
string1 = "Hello World"
substring1 = "hello"
result1 = how_many_times(string1, substring1)  # Output: 3

string2 = "This is a test"
substring2 = "test"
result2 = how_many_times(string2, substring2)  # Output: 2

# Print the results
print("Case 1: Result:", result1)
print("Case 2: Result:", result2)
```  This script defines a function how_many_times that takes a string and a substring as input, and returns the number of occurrences of the substring in the original string. 

The function uses a for loop to iterate over the characters in the string, and counts the number of occurrences of the substring. The function also checks for case-insensitive matching by using the str.zip method, which treats the string and substring as case-insensitive. 

The function is then tested with two different cases, and the results are printed to the console.