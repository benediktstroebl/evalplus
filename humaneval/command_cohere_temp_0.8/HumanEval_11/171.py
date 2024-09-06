```python
def string_xor(a, b):
    return subprocess.check_output(['od', '-A', '2', '-N', '2', '-t', 'u', a + ' ' + b]).decode()
```

This approach takes advantage of the Unix utility `od` (octal dump) to compute the binary XOR of two strings. The `subprocess` module is used to run the `od` command, and the `check_output` function returns the output of the command as a string. The command `od -A 2 -N 2 -t u` is used to interpret the input strings 'a' and 'b' as binary files consisting of 2 bytes per line, upped on each line, and output the binary XOR of these inputs. Note that this approach depends on the specific syntax of the Python script and its environment. 

To run this code, ensure that the required module (`subprocess`) is installed, as it is part of Python's standard library. Thus, if you are using a virtual environment, you may need to activate it. Additionally, ensure that the `od` utility is available in your system, as it typically is in Unix-based systems. 

To use this function, call it with the two strings you want to compute the binary XOR of, and the result will be returned as a string.