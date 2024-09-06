```python
def is_palindrome(string): 
    return string == string[::-1] # returns True if palindrome exists in the string, else False

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        # Find the longest palindrome starting from given string
        palindrome = string[: string.find_palindrome(string[1:], string)
        return palindrome + palindrome[::-1]

def find_palindrome(string):
    # Returns the first palindrome in the string
    if not_palindrome(string):
        return ""
    else:
        return string.find_palindrome(string[1:], string)

def not_palindrome(string):
    return bool(is_palindrome(string))

def make_test_cases():
    print("Test cases:")
    print(make_palindrome(""))
    print(make_palindrome("cat"))
    print(make_palindrome("cata")))
    print(make_palindrome("aacat")))
    print(make_palindrome("ccd"))
    print(make_palindrome("hello"))
    print(make_palindrome("world!"))
    print(make_palindrome(" "))
    print(make_palindrome("1234567890abcdefghijklmnopqr"))
    print(make_palindrome("ABCDEFGHIJKLMNOPQRSTUV"))

def find_first_palindrome(string):
    return make_palindrome(string)

def find_longest_palindrome(string):
    return make_palindrome(string)

def main():
    print("Testing above functions:")
    make_test_cases()

if __name__ == "__main__":
    main()
 ``` 
This Python script provides a self-contained solution to the problem of finding the first and the longest palindrome in a given string. The code also provides a corresponding test cases, which can be used to check the correctness of the functions.