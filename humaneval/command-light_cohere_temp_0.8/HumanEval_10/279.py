Below is a Python script with a self-contained function that solves the problem of creating the longest palindrome from a given string.

```python
# Python program to find the length of a palindrome
def is_palindrome(string):
	# Function to check if a string is palindrome or not
	string = string.lower()  # Convert string to lowercase for case-insensitive comparison
	if string == string[::-1]:
		# If string is palindrome, return True
		return True
	else:
		# If not a palindrome, return False
		return False
def make_palindrome(string):
	# Function to make a palindrome from a given string
	palindrome = ""
	# Add first prefix to palindrome
	palindrome = string[:0] + palindrome
	# Append the reversed string prefix and rest of the string
	palindrome = palindrome + string[::-1]
	return palindrome

# Driver code
print(is_palindrome("inbox"))
print(is_palindrome("box"))
print(is_palindrome("boxcar"))
print(make_palindrome("box"))
print(make_palindrome("boxcar"))
```
This code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome creates the longest palindrome from a given string. The code also provides some test cases to verify the correctness of the function.