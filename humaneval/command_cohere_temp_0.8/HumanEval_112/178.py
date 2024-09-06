```python
def reverse_delete(s, c):
    s_set = set(s)
    c_set = set(c)
    # delete characters in s that are in c
    s = ''.join(char for char in s if char not in c_set)
    # check if the result string is a palindrome
    if s == s[::-1]:
        return s, True
    else:
        return s, False
```

The function `reverse_delete()` takes in two strings, `s` and `c`, and returns a tuple containing the string `s` after deleting characters that are present in `c`, and a boolean indicating whether the resulting string is a palindrome. The `s_set` and `c_set` constructs useets and difference operation to delete characters in `s` that are in `c`. The final line checks if the resulting string is a palindrome by comparing it to its reverse (`s[::-1]`). The boolean value `True` or `False` is returned depending on whether the check is successful. 

This solution works efficiently in O(n) where n is the length of `s` as it only iterates through `s` once to make the set and twice if checking for the palindrome. 

---

Here is a usage example of this function:
```python
print(reverse_delete("abcdedcba", "ab"))
print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
```

The output of this code is as follows: 

```
('cdedc', True)
('bcd', False)
('acdef', False)
```

The function is called three times with the different test cases provided in the problem statement: `abcdedcba` and `ab`, `abcde` and `ae`, and `abcdef` and `b`. In the first call, the resulting string is `cdedc` and it is a palindrome, hence the function returns the tuple (`cdedc`, `True`). In the second call, the resulting string is `bcd` and it is not a palindrome, hence the function returns the tuple (`bcd`, `False`). In the third call, because the string `abcdef` does not have the character `b` it remains the same string and is not a palindrome, and the function returns (`acdef`, `False`). 

The expected output is returned for each call based on the description of the `reverse_delete()` function.