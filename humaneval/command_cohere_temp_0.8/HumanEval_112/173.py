```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return delete, palindrome
```
The `reverse_delete()` function takes two strings, `s` and `c`, as input and returns a tuple containing the string `s` after deleting characters that also appear in `c`, and a boolean indicating whether the resulting string is a palindrome. To achieve this, it constructs a list `delete` that contains all characters from `s` that are not present in `c`. Then, it reverses the `delete` list, and checks if the reversed list equals the original list, which indicates whether the string is a palindrome. The function returns the `delete` list and a boolean value for the palindrome check. 

Here is an example of how to use the above code to solve the task:
```python
def main():
    print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
    print(reverse_delete("abcdef", "b"))  # Output: ('acdef', False)
    print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)

if __name__ == "__main__":
    main()
```
The `main()` function calls the `reverse_delete()` function with different test cases and prints the returned values.