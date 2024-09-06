Here's a Python script that contains a function to solve the given problem:
```python
def solve(N):
    BIN2DEC = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, '-': 36}
    s = 0
    while N > 0:
        s += BIN2DEC[N % 2 * '1' + N // 2 * '0']
        N //= 2
    return format(s, 'b')
```
The function `solve(N)` takes a positive integer `N` as its argument and returns the binary string that is the sum of its binary digits. It converts each digit of the passed integer to its binary counterpart and adds them to a running sum. The function returns the binary string of that sum. The returned value is a string of binary digits, which is the correct output format for the given problem statement.  This approach assumes that the `int` data type internally represents integers in binary format, which is typically the case in most modern programming languages, including Python.  This solution has a time complexity of O(log(N)) since it iterates through each digit of the integer N once, and performs a constant amount of work for each digit, regardless of the digit's value.