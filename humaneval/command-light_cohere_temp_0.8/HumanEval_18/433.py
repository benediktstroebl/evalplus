```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_string = len(string)
    length_substring = len(substring)

    for i in range(1, length_string + 1):
        found = False
        for j in range(1, length_substring + 1):
            if string[i - j] == substring[j - 1]:
                found = True
                count += 1

        if not and found:
            break

    return count

# Test the function
string1 = "aaaa"
string2 = "aa"
string3 = "a"

print("Result for string1:", how_many_times(string1, string1))
print("Result for string2:", how_many_times(string2, string2))
print("Result for string3:", how_many_times(string3, string3))
 ```

The function `how_many_times` takes two parameters: `string` and `substring`. It returns an integer that represents the number of occurrences of the `substring` in the `string`. The function uses two nested loops to iterate over all possible combinations of substrings within the string.