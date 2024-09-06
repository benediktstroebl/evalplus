```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return ''
    lst = []
    while True: 
        pal = False
        for i in range(0,len(string)):
            if string[i] == string[-(i+1)] and not pal: 
                pal = True
                break
        if pal:
            lst.append(string[i: -(i+1)])
        else: 
            break
    return ''.join(''.join(lst[::-1]))

# Test function
def test_make_palindrome(): 
    assert make_palindrome('') == '', "empty string"
    assert make_palindrome('cat') == 'catac', "incorrect result"
    assert make_palindrome('cata') == 'catac', "incorrect result"

# Call test function to run the tests
test_make_palindrome()
 ``` 
This code defines a function `make_palindrome` that finds the shortest palindrome of a string. It also has a tests to ensure the correctness of the function.