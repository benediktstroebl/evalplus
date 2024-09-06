```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f" {0:05d}"*n

# test cases
test_sequence = []
for i in range(0,10):
    test_sequence.append(f"'.join()` + " " + str(i))

print(f"\nTest Results:")
for x in test_sequence:
    print(f"{x}\n")

def main():
    n = int(input("Enter value of n: "))
    print(f"Your string sequence is: {string_sequence(n)}")

main()
``` 
This Python script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-separated numbers from 0 to n. The function uses the string formatting with `05d` to create the string representation of numbers from 0 to n. 

The script then defines a series of test cases using the `test_sequence` list comprehension, each containing a string literal and a space. The test results are printed to the console after each test case. 
The `main` function takes user input for the value of n, and calls the `string_sequence` function to generate and print the corresponding string sequence.