```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the resultant string is a palindrome
    return (''.join(result), result == result[::-1])
```

This approach uses list comprehension to filter the characters of the string `s` that are not present in string `c`.
Then, the resultant string is checked for being a palindrome by comparing it with its reverse using the slice notation `[::-1]`.

The code may be accompanied by tests such as:
```python
# Tests
assert reverse_delete("abcde", "ae") == ('bcd', False)
assert reverse_delete("abcdef", "b") == ('acdef', False)
assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
``` 
Such tests allow you to check your function's correctness and ensure it satisfies the conditions laid out in the problem statement. 
If the problem allows, it is always a good practice to add test cases with a variety of inputs to test the resilience of your solution.