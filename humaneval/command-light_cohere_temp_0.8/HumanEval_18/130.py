```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function that finds how many times a given substring can be found in the original string, accounting for overlapping occurrences.
    """
   
    use a `recur` module to find occurrences:
    counter = Counter(re.findall(substring, string))
    return len(counter)

# Test the function with various inputs
string1 = "aaaaaaa"
string2 = "aaaaaa"
string3 = "aaaaaa123"
substring1 = "a"
substring2 = "aa"
substring3 = "a12345"

count1 = how_many_times(string1, substring1)
count2 = how_many_times(string2, substring2)
count3 = how_many_times(string3, substring3)

print(f"Count of '{string1}' using '{substring1}': {count1}")
print(f"Count of '{string2}' using '{substring2}': {count2}")
print(f"Count of '{string3}' using '{substring3}': {count3}")
``` 
This script defines a function `how_many_times` which finds the count of occurrences of a given substring in a given string, accounting for cases where the substring appears multiple times. The script then uses this `re` module to find these occurrences and returns the count. 

The script also provides test cases for the function, and prints the results.