```python
def flip_case(string):
    return ''.join(''.swapcase(string))

print(flip_case('hello')) # HEllO
print(flip_case('world')) # wORLD
print(flip_case('SSLarounds'))# sSLLAROONs
print(flip_case('cohere'))# coREHeRe
print(flip_case('Unicased'))# UNIcasED
```